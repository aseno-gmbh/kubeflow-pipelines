# Copyright 2022 The Kubeflow Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from google_cloud_pipeline_components.types import artifact_types
from kfp import components
from kfp import dsl
from kfp.components import importer_node
from kfp.dsl import Input

project_root = os.path.abspath(os.path.join(__file__, *([os.path.pardir] * 6)))
component_path = os.path.join(project_root, 'components', 'google-cloud',
                              'google_cloud_pipeline_components', 'v1', 'model',
                              'upload_model', 'component.yaml')
gcpc_component = components.load_component_from_file(component_path)


@dsl.component(
    kfp_package_path='git+https://github.com/connor-mccarthy/pipelines@support-custom-artifact-types#subdirectory=sdk/python',
    packages_to_install=[
        'git+https://github.com/connor-mccarthy/pipelines@support-custom-artifact-types#subdirectory=components/google-cloud'
    ],
)
def dummy_op(artifact: Input[artifact_types.UnmanagedContainerModel]):
    print('artifact.type: ', type(artifact))
    print('artifact.name: ', artifact.name)
    print('artifact.uri: ', artifact.uri)
    print('artifact.metadata: ', artifact.metadata)


@dsl.pipeline(
    name='test-custom-artifact',
    pipeline_root='gs://cjmccarthy-kfp-default-bucket')
def my_pipeline():
    importer_spec = importer_node.importer(
        artifact_uri='gs://managed-pipeline-gcpc-e2e-test/automl-tabular/model',
        artifact_class=artifact_types.UnmanagedContainerModel,
        metadata={
            'containerSpec': {
                'imageUri':
                    'us-docker.pkg.dev/vertex-ai/automl-tabular/prediction-server:prod'
            }
        })

    dummy_op(artifact=importer_spec.outputs['artifact'])


if __name__ == '__main__':
    from kfp import compiler
    ir_file = __file__.replace('.py', '.yaml')
    compiler.Compiler().compile(pipeline_func=my_pipeline, package_path=ir_file)
