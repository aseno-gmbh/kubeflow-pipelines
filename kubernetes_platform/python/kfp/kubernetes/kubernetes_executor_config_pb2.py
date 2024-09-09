# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kubernetes_executor_config.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n kubernetes_executor_config.proto\x12\x0ekfp_kubernetes\x1a\x1cgoogle/protobuf/struct.proto\"\xb4\x07\n\x18KubernetesExecutorConfig\x12\x38\n\x10secret_as_volume\x18\x01 \x03(\x0b\x32\x1e.kfp_kubernetes.SecretAsVolume\x12\x32\n\rsecret_as_env\x18\x02 \x03(\x0b\x32\x1b.kfp_kubernetes.SecretAsEnv\x12+\n\tpvc_mount\x18\x03 \x03(\x0b\x32\x18.kfp_kubernetes.PvcMount\x12\x33\n\rnode_selector\x18\x04 \x01(\x0b\x32\x1c.kfp_kubernetes.NodeSelector\x12\x31\n\x0cpod_metadata\x18\x05 \x01(\x0b\x32\x1b.kfp_kubernetes.PodMetadata\x12:\n\x11image_pull_secret\x18\x06 \x03(\x0b\x32\x1f.kfp_kubernetes.ImagePullSecret\x12\x19\n\x11image_pull_policy\x18\x07 \x01(\t\x12?\n\x14\x63onfig_map_as_volume\x18\x08 \x03(\x0b\x32!.kfp_kubernetes.ConfigMapAsVolume\x12\x39\n\x11\x63onfig_map_as_env\x18\t \x03(\x0b\x32\x1e.kfp_kubernetes.ConfigMapAsEnv\x12\x1f\n\x17\x61\x63tive_deadline_seconds\x18\n \x01(\x03\x12\x39\n\x11\x66ield_path_as_env\x18\x0b \x03(\x0b\x32\x1e.kfp_kubernetes.FieldPathAsEnv\x12/\n\x0btolerations\x18\x0c \x03(\x0b\x32\x1a.kfp_kubernetes.Toleration\x12H\n\x18generic_ephemeral_volume\x18\r \x03(\x0b\x32&.kfp_kubernetes.GenericEphemeralVolume\x12\x37\n\rnode_affinity\x18\x0e \x03(\x0b\x32 .kfp_kubernetes.NodeAffinityTerm\x12\x35\n\x0cpod_affinity\x18\x0f \x03(\x0b\x32\x1f.kfp_kubernetes.PodAffinityTerm\x12\x42\n\x15\x65nabled_shared_memory\x18\x10 \x01(\x0b\x32#.kfp_kubernetes.EnabledSharedMemory\x12\x37\n\x10\x65mpty_dir_mounts\x18\x11 \x03(\x0b\x32\x1d.kfp_kubernetes.EmptyDirMount\"8\n\x13\x45nabledSharedMemory\x12\x13\n\x0bvolume_name\x18\x01 \x01(\t\x12\x0c\n\x04size\x18\x02 \x01(\t\"]\n\x0eSecretAsVolume\x12\x13\n\x0bsecret_name\x18\x01 \x01(\t\x12\x12\n\nmount_path\x18\x02 \x01(\t\x12\x15\n\x08optional\x18\x03 \x01(\x08H\x00\x88\x01\x01\x42\x0b\n\t_optional\"\x9f\x01\n\x0bSecretAsEnv\x12\x13\n\x0bsecret_name\x18\x01 \x01(\t\x12\x41\n\nkey_to_env\x18\x02 \x03(\x0b\x32-.kfp_kubernetes.SecretAsEnv.SecretKeyToEnvMap\x1a\x38\n\x11SecretKeyToEnvMap\x12\x12\n\nsecret_key\x18\x01 \x01(\t\x12\x0f\n\x07\x65nv_var\x18\x02 \x01(\t\"N\n\x17TaskOutputParameterSpec\x12\x15\n\rproducer_task\x18\x01 \x01(\t\x12\x1c\n\x14output_parameter_key\x18\x02 \x01(\t\"\xb2\x01\n\x08PvcMount\x12H\n\x15task_output_parameter\x18\x01 \x01(\x0b\x32\'.kfp_kubernetes.TaskOutputParameterSpecH\x00\x12\x12\n\x08\x63onstant\x18\x02 \x01(\tH\x00\x12#\n\x19\x63omponent_input_parameter\x18\x03 \x01(\tH\x00\x12\x12\n\nmount_path\x18\x04 \x01(\tB\x0f\n\rpvc_reference\"\xe4\x01\n\tCreatePvc\x12\x12\n\x08pvc_name\x18\x01 \x01(\tH\x00\x12\x19\n\x0fpvc_name_suffix\x18\x02 \x01(\tH\x00\x12\x14\n\x0c\x61\x63\x63\x65ss_modes\x18\x03 \x03(\t\x12\x0c\n\x04size\x18\x04 \x01(\t\x12\x1d\n\x15\x64\x65\x66\x61ult_storage_class\x18\x05 \x01(\x08\x12\x1a\n\x12storage_class_name\x18\x06 \x01(\t\x12\x13\n\x0bvolume_name\x18\x07 \x01(\t\x12,\n\x0b\x61nnotations\x18\x08 \x01(\x0b\x32\x17.google.protobuf.StructB\x06\n\x04name\"\x9f\x01\n\tDeletePvc\x12H\n\x15task_output_parameter\x18\x01 \x01(\x0b\x32\'.kfp_kubernetes.TaskOutputParameterSpecH\x00\x12\x12\n\x08\x63onstant\x18\x02 \x01(\tH\x00\x12#\n\x19\x63omponent_input_parameter\x18\x03 \x01(\tH\x00\x42\x0f\n\rpvc_reference\"w\n\x0cNodeSelector\x12\x38\n\x06labels\x18\x01 \x03(\x0b\x32(.kfp_kubernetes.NodeSelector.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xec\x01\n\x0bPodMetadata\x12\x37\n\x06labels\x18\x01 \x03(\x0b\x32\'.kfp_kubernetes.PodMetadata.LabelsEntry\x12\x41\n\x0b\x61nnotations\x18\x02 \x03(\x0b\x32,.kfp_kubernetes.PodMetadata.AnnotationsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x32\n\x10\x41nnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"d\n\x11\x43onfigMapAsVolume\x12\x17\n\x0f\x63onfig_map_name\x18\x01 \x01(\t\x12\x12\n\nmount_path\x18\x02 \x01(\t\x12\x15\n\x08optional\x18\x03 \x01(\x08H\x00\x88\x01\x01\x42\x0b\n\t_optional\"\xb3\x01\n\x0e\x43onfigMapAsEnv\x12\x17\n\x0f\x63onfig_map_name\x18\x01 \x01(\t\x12G\n\nkey_to_env\x18\x02 \x03(\x0b\x32\x33.kfp_kubernetes.ConfigMapAsEnv.ConfigMapKeyToEnvMap\x1a?\n\x14\x43onfigMapKeyToEnvMap\x12\x16\n\x0e\x63onfig_map_key\x18\x01 \x01(\t\x12\x0f\n\x07\x65nv_var\x18\x02 \x01(\t\"\xcf\x01\n\x16GenericEphemeralVolume\x12\x13\n\x0bvolume_name\x18\x01 \x01(\t\x12\x12\n\nmount_path\x18\x02 \x01(\t\x12\x14\n\x0c\x61\x63\x63\x65ss_modes\x18\x03 \x03(\t\x12\x0c\n\x04size\x18\x04 \x01(\t\x12\x1d\n\x15\x64\x65\x66\x61ult_storage_class\x18\x05 \x01(\x08\x12\x1a\n\x12storage_class_name\x18\x06 \x01(\t\x12-\n\x08metadata\x18\x07 \x01(\x0b\x32\x1b.kfp_kubernetes.PodMetadata\"&\n\x0fImagePullSecret\x12\x13\n\x0bsecret_name\x18\x01 \x01(\t\"2\n\x0e\x46ieldPathAsEnv\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nfield_path\x18\x02 \x01(\t\"\x82\x01\n\nToleration\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x10\n\x08operator\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\x12\x0e\n\x06\x65\x66\x66\x65\x63t\x18\x04 \x01(\t\x12\x1f\n\x12toleration_seconds\x18\x05 \x01(\x03H\x00\x88\x01\x01\x42\x15\n\x13_toleration_seconds\"D\n\x13SelectorRequirement\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x10\n\x08operator\x18\x02 \x01(\t\x12\x0e\n\x06values\x18\x03 \x03(\t\"\xad\x01\n\x10NodeAffinityTerm\x12>\n\x11match_expressions\x18\x01 \x03(\x0b\x32#.kfp_kubernetes.SelectorRequirement\x12\x39\n\x0cmatch_fields\x18\x02 \x03(\x0b\x32#.kfp_kubernetes.SelectorRequirement\x12\x13\n\x06weight\x18\x03 \x01(\x05H\x00\x88\x01\x01\x42\t\n\x07_weight\"\xa3\x04\n\x0fPodAffinityTerm\x12\x42\n\x15match_pod_expressions\x18\x01 \x03(\x0b\x32#.kfp_kubernetes.SelectorRequirement\x12M\n\x10match_pod_labels\x18\x02 \x03(\x0b\x32\x33.kfp_kubernetes.PodAffinityTerm.MatchPodLabelsEntry\x12\x14\n\x0ctopology_key\x18\x03 \x01(\t\x12\x12\n\nnamespaces\x18\x04 \x03(\t\x12H\n\x1bmatch_namespace_expressions\x18\x05 \x03(\x0b\x32#.kfp_kubernetes.SelectorRequirement\x12Y\n\x16match_namespace_labels\x18\x06 \x03(\x0b\x32\x39.kfp_kubernetes.PodAffinityTerm.MatchNamespaceLabelsEntry\x12\x13\n\x06weight\x18\x07 \x01(\x05H\x00\x88\x01\x01\x12\x11\n\x04\x61nti\x18\x08 \x01(\x08H\x01\x88\x01\x01\x1a\x35\n\x13MatchPodLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a;\n\x19MatchNamespaceLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\t\n\x07_weightB\x07\n\x05_anti\"\x80\x01\n\rEmptyDirMount\x12\x13\n\x0bvolume_name\x18\x01 \x01(\t\x12\x12\n\nmount_path\x18\x02 \x01(\t\x12\x13\n\x06medium\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x17\n\nsize_limit\x18\x04 \x01(\tH\x01\x88\x01\x01\x42\t\n\x07_mediumB\r\n\x0b_size_limitBIZGgithub.com/kubeflow/pipelines/kubernetes_platform/go/kubernetesplatformb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'kubernetes_executor_config_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZGgithub.com/kubeflow/pipelines/kubernetes_platform/go/kubernetesplatform'
  _NODESELECTOR_LABELSENTRY._options = None
  _NODESELECTOR_LABELSENTRY._serialized_options = b'8\001'
  _PODMETADATA_LABELSENTRY._options = None
  _PODMETADATA_LABELSENTRY._serialized_options = b'8\001'
  _PODMETADATA_ANNOTATIONSENTRY._options = None
  _PODMETADATA_ANNOTATIONSENTRY._serialized_options = b'8\001'
  _PODAFFINITYTERM_MATCHPODLABELSENTRY._options = None
  _PODAFFINITYTERM_MATCHPODLABELSENTRY._serialized_options = b'8\001'
  _PODAFFINITYTERM_MATCHNAMESPACELABELSENTRY._options = None
  _PODAFFINITYTERM_MATCHNAMESPACELABELSENTRY._serialized_options = b'8\001'
  _KUBERNETESEXECUTORCONFIG._serialized_start=83
  _KUBERNETESEXECUTORCONFIG._serialized_end=1031
  _ENABLEDSHAREDMEMORY._serialized_start=1033
  _ENABLEDSHAREDMEMORY._serialized_end=1089
  _SECRETASVOLUME._serialized_start=1091
  _SECRETASVOLUME._serialized_end=1184
  _SECRETASENV._serialized_start=1187
  _SECRETASENV._serialized_end=1346
  _SECRETASENV_SECRETKEYTOENVMAP._serialized_start=1290
  _SECRETASENV_SECRETKEYTOENVMAP._serialized_end=1346
  _TASKOUTPUTPARAMETERSPEC._serialized_start=1348
  _TASKOUTPUTPARAMETERSPEC._serialized_end=1426
  _PVCMOUNT._serialized_start=1429
  _PVCMOUNT._serialized_end=1607
  _CREATEPVC._serialized_start=1610
  _CREATEPVC._serialized_end=1838
  _DELETEPVC._serialized_start=1841
  _DELETEPVC._serialized_end=2000
  _NODESELECTOR._serialized_start=2002
  _NODESELECTOR._serialized_end=2121
  _NODESELECTOR_LABELSENTRY._serialized_start=2076
  _NODESELECTOR_LABELSENTRY._serialized_end=2121
  _PODMETADATA._serialized_start=2124
  _PODMETADATA._serialized_end=2360
  _PODMETADATA_LABELSENTRY._serialized_start=2076
  _PODMETADATA_LABELSENTRY._serialized_end=2121
  _PODMETADATA_ANNOTATIONSENTRY._serialized_start=2310
  _PODMETADATA_ANNOTATIONSENTRY._serialized_end=2360
  _CONFIGMAPASVOLUME._serialized_start=2362
  _CONFIGMAPASVOLUME._serialized_end=2462
  _CONFIGMAPASENV._serialized_start=2465
  _CONFIGMAPASENV._serialized_end=2644
  _CONFIGMAPASENV_CONFIGMAPKEYTOENVMAP._serialized_start=2581
  _CONFIGMAPASENV_CONFIGMAPKEYTOENVMAP._serialized_end=2644
  _GENERICEPHEMERALVOLUME._serialized_start=2647
  _GENERICEPHEMERALVOLUME._serialized_end=2854
  _IMAGEPULLSECRET._serialized_start=2856
  _IMAGEPULLSECRET._serialized_end=2894
  _FIELDPATHASENV._serialized_start=2896
  _FIELDPATHASENV._serialized_end=2946
  _TOLERATION._serialized_start=2949
  _TOLERATION._serialized_end=3079
  _SELECTORREQUIREMENT._serialized_start=3081
  _SELECTORREQUIREMENT._serialized_end=3149
  _NODEAFFINITYTERM._serialized_start=3152
  _NODEAFFINITYTERM._serialized_end=3325
  _PODAFFINITYTERM._serialized_start=3328
  _PODAFFINITYTERM._serialized_end=3875
  _PODAFFINITYTERM_MATCHPODLABELSENTRY._serialized_start=3741
  _PODAFFINITYTERM_MATCHPODLABELSENTRY._serialized_end=3794
  _PODAFFINITYTERM_MATCHNAMESPACELABELSENTRY._serialized_start=3796
  _PODAFFINITYTERM_MATCHNAMESPACELABELSENTRY._serialized_end=3855
  _EMPTYDIRMOUNT._serialized_start=3878
  _EMPTYDIRMOUNT._serialized_end=4006
# @@protoc_insertion_point(module_scope)
