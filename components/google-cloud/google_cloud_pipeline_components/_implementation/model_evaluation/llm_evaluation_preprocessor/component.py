# Copyright 2023 The Kubeflow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""LLM Eval Preprocessor Component for Converting Eval Dataset Format."""

from typing import List, NamedTuple

from google_cloud_pipeline_components import utils as gcpc_utils
from google_cloud_pipeline_components._implementation.model_evaluation import utils
from google_cloud_pipeline_components._implementation.model_evaluation import version
from kfp import dsl


# pylint: disable=g-import-not-at-top, g-doc-args, unexpected-keyword-arg
@dsl.component(base_image=version.LLM_EVAL_IMAGE_TAG)
def add_json_escape_to_list(input_list: List[str]) -> str:
  import json

  json_escaped_list = json.dumps(input_list).replace('"', '\\"')
  return json_escaped_list


@dsl.container_component
def evaluation_dataset_preprocessor_internal(
    project: str,
    location: str,
    gcs_source_uris: str,
    output_dirs: dsl.OutputPath(list),
    gcp_resources: dsl.OutputPath(str),
    input_field_name: str = 'input_text',
    role_field_name: str = 'role',
    model_name: str = 'publishers/google/model/text-bison@002',
    display_name: str = 'llm_evaluation_dataset_preprocessor_component',
    machine_type: str = 'e2-highmem-16',
    service_account: str = '',
    network: str = '',
    encryption_spec_key_name: str = '',
):
  # fmt: off
  """Preprocesses Eval Dataset format.

  This component adds a `prompt` field for running Batch Prediction component on
  the eval dataset. This component is used in LLM Evaluation pipelines.

  Args:
      project: Required. The GCP project that runs the pipeline component.
      location: Required. The GCP region that runs the pipeline component.
      gcs_source_uris: A json escaped list of GCS URIs of the input eval dataset.
      input_field_name: The field name of the input eval dataset instances that
        contains the input prompts to the LLM.
      role_field_name: The field name of the role for input eval dataset instances
        that contains the input prompts to the LLM.
      model_name: Name of the model being used to create model-specific schemas.
      machine_type: The machine type of this custom job. If not set, defaulted
        to `e2-highmem-16`. More details:
        https://cloud.google.com/compute/docs/machine-resource
      service_account: Sets the default service account for workload run-as
        account. The service account running the pipeline
        (https://cloud.google.com/vertex-ai/docs/pipelines/configure-project#service-account)
        submitting jobs must have act-as permission on this run-as account. If
        unspecified, the Vertex AI Custom Code Service
        Agent(https://cloud.google.com/vertex-ai/docs/general/access-control#service-agents)
        for the CustomJob's project.
      network: The full name of the Compute Engine network to which the job
        should be peered. For example, projects/12345/global/networks/myVPC.
        Format is of the form projects/{project}/global/networks/{network}.
        Where {project} is a project number, as in 12345, and {network} is a
        network name. Private services access must already be configured for the
        network. If left unspecified, the job is not peered with any network.
      encryption_spec_key_name: Customer-managed encryption key options for the
        CustomJob. If this is set, then all resources created by the CustomJob
        will be encrypted with the provided encryption key.
  Returns:
      output_dirs: A list of GCS directories where the output files will be
        stored, generated by the pipeline.
      gcp_resources: Serialized gcp_resources proto tracking the custom job.
  """
  # fmt: on
  return gcpc_utils.build_serverless_customjob_container_spec(
      project=project,
      location=location,
      custom_job_payload=utils.build_custom_job_payload(
          display_name=display_name,
          machine_type=machine_type,
          image_uri=version.LLM_EVAL_IMAGE_TAG,
          args=[
              f'--eval_dataset_preprocessor={True}',
              f'--gcs_source_uris={gcs_source_uris}',
              f'--input_field_name={input_field_name}',
              f'--role_field_name={role_field_name}',
              f'--model_name={model_name}',
              f'--output_dirs={output_dirs}',
              '--executor_input={{$.json_escape[1]}}',
          ],
          service_account=service_account,
          network=network,
          encryption_spec_key_name=encryption_spec_key_name,
      ),
      gcp_resources=gcp_resources,
  )


@dsl.pipeline(name='LLMEvaluationPreprocessorOp')
def llm_evaluation_dataset_preprocessor_graph_component(
    project: str,
    location: str,
    gcs_source_uris: List[str],
    input_field_name: str = 'input_text',
    role_field_name: str = 'role',
    model_name: str = 'publishers/google/model/text-bison@002',
    display_name: str = 'llm_evaluation_dataset_preprocessor_component',
    machine_type: str = 'e2-standard-4',
    service_account: str = '',
    network: str = '',
    encryption_spec_key_name: str = '',
) -> NamedTuple('outputs', preprocessed_gcs_source_uris=List[str]):
  """Graph component for Eval Dataset Preprocesser.

  This component adds a `prompt` field for running Batch Prediction component on
  the eval dataset. This component is used in LLM Evaluation pipelines.

  Args:
      project: Required. The GCP project that runs the pipeline component.
      location: Required. The GCP region that runs the pipeline component.
      gcs_source_uris: A list of GCS URIs of the input eval dataset.
      input_field_name: The field name of the input eval dataset instances that
        contains the input prompts to the LLM.
      role_field_name: The field name of the role for input eval dataset
        instances that contains the input prompts to the LLM.
      model_name: Name of the model being used to create model-specific schemas.
      display_name: The name of the Evaluation job.
      machine_type: The machine type of this custom job. If not set, defaulted
        to `e2-standard-4`. More details:
        https://cloud.google.com/compute/docs/machine-resource
      service_account: Sets the default service account for workload run-as
        account. The service account running the pipeline
        (https://cloud.google.com/vertex-ai/docs/pipelines/configure-project#service-account)
        submitting jobs must have act-as permission on this run-as account. If
        unspecified, the Vertex AI Custom Code Service
        Agent(https://cloud.google.com/vertex-ai/docs/general/access-control#service-agents)
        for the CustomJob's project.
      network: The full name of the Compute Engine network to which the job
        should be peered. For example, projects/12345/global/networks/myVPC.
        Format is of the form projects/{project}/global/networks/{network}.
        Where {project} is a project number, as in 12345, and {network} is a
        network name. Private services access must already be configured for the
        network. If left unspecified, the job is not peered with any network.
      encryption_spec_key_name: Customer-managed encryption key options for the
        CustomJob. If this is set, then all resources created by the CustomJob
        will be encrypted with the provided encryption key.

  Returns:
      preprocessed_gcs_source_uris: A list of GCS directories where the
        preprocessed eval dataset files will be stored..
  """
  outputs = NamedTuple(
      'outputs',
      preprocessed_gcs_source_uris=List[str],
  )

  eval_dataset_preprocessor_task = evaluation_dataset_preprocessor_internal(
      project=project,
      location=location,
      gcs_source_uris=add_json_escape_to_list(
          input_list=gcs_source_uris
      ).output,
      input_field_name=input_field_name,
      role_field_name=role_field_name,
      model_name=model_name,
      display_name=display_name,
      machine_type=machine_type,
      service_account=service_account,
      network=network,
      encryption_spec_key_name=encryption_spec_key_name,
  )

  return outputs(
      preprocessed_gcs_source_uris=eval_dataset_preprocessor_task.outputs[
          'output_dirs'
      ]
  )
