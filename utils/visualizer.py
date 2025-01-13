from diagrams import Diagram
import pydot
from utils.files import upload_image
from diagrams.aws.analytics import (
    AmazonOpensearchService,
    Analytics,
    Athena,
    CloudsearchSearchDocuments,
    Cloudsearch,
    DataLakeResource,
    DataPipeline,
    ElasticsearchService,
    EMRCluster,
    EMREngineMaprM3,
    EMREngineMaprM5,
    EMREngineMaprM7,
    EMREngine,
    EMRHdfsCluster,
    EMR,
    GlueCrawlers,
    GlueDataCatalog,
    Glue,
    KinesisDataAnalytics,
    KinesisDataFirehose,
    KinesisDataStreams,
    KinesisVideoStreams,
    Kinesis,
    LakeFormation,
    ManagedStreamingForKafka,
    Quicksight,
)
from diagrams.aws.compute import (
    AppRunner,
    ApplicationAutoScaling,
    Batch,
    ComputeOptimizer,
    Compute,
    EC2Ami,
    EC2AutoScaling,
    EC2ContainerRegistryImage,
    EC2ContainerRegistryRegistry,
    EC2ContainerRegistry,
    EC2ElasticIpAddress,
    EC2ImageBuilder,
    EC2Instance,
    EC2Instances,
    EC2Rescue,
    EC2SpotInstance,
    EC2,
    ElasticBeanstalkApplication,
    ElasticBeanstalkDeployment,
    ElasticBeanstalk,
    ElasticContainerServiceContainer,
    ElasticContainerServiceService,
    ElasticContainerService,
    ElasticKubernetesService,
    Fargate,
    LambdaFunction,
    Lambda,
    Lightsail,
    LocalZones,
    Outposts,
    ServerlessApplicationRepository,
    ThinkboxDeadline,
    ThinkboxDraft,
    ThinkboxFrost,
    ThinkboxKrakatoa,
    ThinkboxSequoia,
    ThinkboxStoke,
    ThinkboxXmesh,
    VmwareCloudOnAWS,
    Wavelength,
)
from diagrams.aws.network import (
    APIGatewayEndpoint,
    APIGateway,
    AppMesh,
    ClientVpn,
    CloudMap,
    CloudFrontDownloadDistribution,
    CloudFrontEdgeLocation,
    CloudFrontStreamingDistribution,
    CloudFront,
    DirectConnect,
    ElasticLoadBalancing,
    ElbApplicationLoadBalancer,
    ElbClassicLoadBalancer,
    ElbNetworkLoadBalancer,
    Endpoint,
    GlobalAccelerator,
    Nacl,
    NATGateway,
    NetworkFirewall,
    NetworkingAndContentDelivery,
    PrivateSubnet,
    Privatelink,
    PublicSubnet,
    Route53HostedZone,
    Route53,
    RouteTable,
    SiteToSiteVpn,
    TransitGateway,
    VPCCustomerGateway,
    VPCElasticNetworkAdapter,
    VPCElasticNetworkInterface,
    VPCFlowLogs,
    VPCPeering,
    VPCRouter,
    VPCTrafficMirroring,
    VPC,
    VpnConnection,
    VpnGateway,
)
from diagrams.aws.database import (
    AuroraInstance,
    Aurora,
    DatabaseMigrationServiceDatabaseMigrationWorkflow,
    DatabaseMigrationService,
    Database,
    DocumentdbMongodbCompatibility,
    DynamodbAttribute,
    DynamodbAttributes,
    DynamodbDax,
    DynamodbGlobalSecondaryIndex,
    DynamodbItem,
    DynamodbItems,
    DynamodbTable,
    Dynamodb,
    ElasticacheCacheNode,
    ElasticacheForMemcached,
    ElasticacheForRedis,
    Elasticache,
    KeyspacesManagedApacheCassandraService,
    Neptune,
    QuantumLedgerDatabaseQldb,
    RDSInstance,
    RDSMariadbInstance,
    RDSMysqlInstance,
    RDSOnVmware,
    RDSOracleInstance,
    RDSPostgresqlInstance,
    RDSSqlServerInstance,
    RDS,
    RedshiftDenseComputeNode,
    RedshiftDenseStorageNode,
    Redshift,
    Timestream,
)
from diagrams.aws.general import (
    Client,
    Disk,
    Forums,
    General,
    GenericDatabase,
    GenericFirewall,
    GenericOfficeBuilding,
    GenericSamlToken,
    GenericSDK,
    InternetAlt1,
    InternetAlt2,
    InternetGateway,
    Marketplace,
    MobileClient,
    Multimedia,
    OfficeBuilding,
    SamlToken,
    SDK,
    SslPadlock,
    TapeStorage,
    Toolkit,
    TraditionalServer,
    User,
    Users,
)

from diagrams.aws.management import (
    AmazonDevopsGuru,
    AmazonManagedGrafana,
    AmazonManagedPrometheus,
    AmazonManagedWorkflowsApacheAirflow,
    AutoScaling,
    Chatbot,
    CloudformationChangeSet,
    CloudformationStack,
    CloudformationTemplate,
    Cloudformation,
    Cloudtrail,
    CloudwatchAlarm,
    CloudwatchEventEventBased,
    CloudwatchEventTimeBased,
    CloudwatchRule,
    Cloudwatch,
    Codeguru,
    CommandLineInterface,
    Config,
    ControlTower,
    LicenseManager,
    ManagedServices,
    ManagementAndGovernance,
    ManagementConsole,
    OpsworksApps,
    OpsworksDeployments,
    OpsworksInstances,
    OpsworksLayers,
    OpsworksMonitoring,
    OpsworksPermissions,
    OpsworksResources,
    OpsworksStack,
    Opsworks,
    OrganizationsAccount,
    OrganizationsOrganizationalUnit,
    Organizations,
    PersonalHealthDashboard,
    Proton,
    ServiceCatalog,
    SystemsManagerAppConfig,
    SystemsManagerAutomation,
    SystemsManagerDocuments,
    SystemsManagerInventory,
    SystemsManagerMaintenanceWindows,
    SystemsManagerOpscenter,
    SystemsManagerParameterStore,
    SystemsManagerPatchManager,
    SystemsManagerRunCommand,
    SystemsManagerStateManager,
    SystemsManager,
    TrustedAdvisorChecklistCost,
    TrustedAdvisorChecklistFaultTolerant,
    TrustedAdvisorChecklistPerformance,
    TrustedAdvisorChecklistSecurity,
    TrustedAdvisorChecklist,
    TrustedAdvisor,
    WellArchitectedTool,
)

from diagrams.aws.storage import (
    Backup,
    CloudendureDisasterRecovery,
    EFSInfrequentaccessPrimaryBg,
    EFSStandardPrimaryBg,
    ElasticBlockStoreEBSSnapshot,
    ElasticBlockStoreEBSVolume,
    ElasticBlockStoreEBS,
    ElasticFileSystemEFSFileSystem,
    ElasticFileSystemEFS,
    FsxForLustre,
    FsxForWindowsFileServer,
    Fsx,
    MultipleVolumesResource,
    S3GlacierArchive,
    S3GlacierVault,
    S3Glacier,
    SimpleStorageServiceS3BucketWithObjects,
    SimpleStorageServiceS3Bucket,
    SimpleStorageServiceS3Object,
    SimpleStorageServiceS3,
    SnowFamilySnowballImportExport,
    SnowballEdge,
    Snowball,
    Snowmobile,
    StorageGatewayCachedVolume,
    StorageGatewayNonCachedVolume,
    StorageGatewayVirtualTapeLibrary,
    StorageGateway,
    Storage,
)

from diagrams.aws.security import (
    AdConnector,
    Artifact,
    CertificateAuthority,
    CertificateManager,
    CloudDirectory,
    Cloudhsm,
    Cognito,
    Detective,
    DirectoryService,
    FirewallManager,
    Guardduty,
    IdentityAndAccessManagementIamAccessAnalyzer,
    IdentityAndAccessManagementIamAddOn,
    IdentityAndAccessManagementIamAWSStsAlternate,
    IdentityAndAccessManagementIamAWSSts,
    IdentityAndAccessManagementIamDataEncryptionKey,
    IdentityAndAccessManagementIamEncryptedData,
    IdentityAndAccessManagementIamLongTermSecurityCredential,
    IdentityAndAccessManagementIamMfaToken,
    IdentityAndAccessManagementIamPermissions,
    IdentityAndAccessManagementIamRole,
    IdentityAndAccessManagementIamTemporarySecurityCredential,
    IdentityAndAccessManagementIam,
    InspectorAgent,
    Inspector,
    KeyManagementService,
    Macie,
    ManagedMicrosoftAd,
    ResourceAccessManager,
    SecretsManager,
    SecurityHubFinding,
    SecurityHub,
    SecurityIdentityAndCompliance,
    ShieldAdvanced,
    Shield,
    SimpleAd,
    SingleSignOn,
    WAFFilteringRule,
    WAF,
)

from utils.files import openfile, readfile

resource_icon_map = {
    "aws_ad_connector": AdConnector,
    "aws_artifact": Artifact,
    "aws_certificate_authority": CertificateAuthority,
    "aws_acm": CertificateManager,
    "aws_cloud_directory": CloudDirectory,
    "aws_cloudhsm": Cloudhsm,
    "aws_cognito": Cognito,
    "aws_detective": Detective,
    "aws_directory_service": DirectoryService,
    "aws_firewall_manager": FirewallManager,
    "aws_guardduty": Guardduty,
    "aws_iam_access_analyzer": IdentityAndAccessManagementIamAccessAnalyzer,
    "aws_iam_addon": IdentityAndAccessManagementIamAddOn,
    "aws_iam_aws_sts_alternate": IdentityAndAccessManagementIamAWSStsAlternate,
    "aws_iam_aws_sts": IdentityAndAccessManagementIamAWSSts,
    "aws_iam_data_encryption_key": IdentityAndAccessManagementIamDataEncryptionKey,
    "aws_iam_encrypted_data": IdentityAndAccessManagementIamEncryptedData,
    "aws_iam_long_term_security_credential": IdentityAndAccessManagementIamLongTermSecurityCredential,
    "aws_iam_mfa_token": IdentityAndAccessManagementIamMfaToken,
    "aws_iam_permissions": IdentityAndAccessManagementIamPermissions,
    "aws_iam_role": IdentityAndAccessManagementIamRole,
    "aws_iam_temporary_security_credential": IdentityAndAccessManagementIamTemporarySecurityCredential,
    "aws_iam": IdentityAndAccessManagementIam,
    "aws_iam_role_policy_attachment": IdentityAndAccessManagementIamRole,
    "aws_inspector_agent": InspectorAgent,
    "aws_inspector": Inspector,
    "aws_kms": KeyManagementService,
    "aws_macie": Macie,
    "aws_managed_microsoft_ad": ManagedMicrosoftAd,
    "aws_resource_access_manager": ResourceAccessManager,
    "aws_secrets_manager": SecretsManager,
    "aws_security_hub_finding": SecurityHubFinding,
    "aws_security_group.lb_sg": SecurityHub,
    "aws_security_identity_compliance": SecurityIdentityAndCompliance,
    "aws_shield_advanced": ShieldAdvanced,
    "aws_shield": Shield,
    "aws_simple_ad": SimpleAd,
    "aws_single_sign_on": SingleSignOn,
    "aws_waf_filtering_rule": WAFFilteringRule,
    "aws_waf": WAF,
    "aws_backup": Backup,
    "aws_cloudendure_disaster_recovery": CloudendureDisasterRecovery,
    "aws_efs_infrequent_access_primary": EFSInfrequentaccessPrimaryBg,
    "aws_efs_standard_primary": EFSStandardPrimaryBg,
    "aws_ebs_snapshot": ElasticBlockStoreEBSSnapshot,
    "aws_ebs_volume": ElasticBlockStoreEBSVolume,
    "aws_ebs": ElasticBlockStoreEBS,
    "aws_efs_file_system": ElasticFileSystemEFSFileSystem,
    "aws_efs": ElasticFileSystemEFS,
    "aws_fsx_for_lustre": FsxForLustre,
    "aws_fsx_for_windows": FsxForWindowsFileServer,
    "aws_fsx": Fsx,
    "aws_multiple_volumes": MultipleVolumesResource,
    "aws_s3_glacier_archive": S3GlacierArchive,
    "aws_s3_glacier_vault": S3GlacierVault,
    "aws_s3_glacier": S3Glacier,
    "aws_s3_bucket_with_objects": SimpleStorageServiceS3BucketWithObjects,
    "aws_s3_bucket": SimpleStorageServiceS3Bucket,
    "aws_s3_object": SimpleStorageServiceS3Object,
    "aws_s3": SimpleStorageServiceS3,
    "aws_snow_family_snowball_import_export": SnowFamilySnowballImportExport,
    "aws_snowball_edge": SnowballEdge,
    "aws_snowball": Snowball,
    "aws_snowmobile": Snowmobile,
    "aws_storage_gateway_cached_volume": StorageGatewayCachedVolume,
    "aws_storage_gateway_non_cached_volume": StorageGatewayNonCachedVolume,
    "aws_storage_gateway_virtual_tape_library": StorageGatewayVirtualTapeLibrary,
    "aws_storage_gateway": StorageGateway,
    "aws_storage": Storage,
    "aws_devops_guru": AmazonDevopsGuru,
    "aws_managed_grafana": AmazonManagedGrafana,
    "aws_managed_prometheus": AmazonManagedPrometheus,
    "aws_managed_workflows_apache_airflow": AmazonManagedWorkflowsApacheAirflow,
    "aws_autoscaling": AutoScaling,
    "aws_chatbot": Chatbot,
    "aws_cloudformation_change_set": CloudformationChangeSet,
    "aws_cloudformation_stack": CloudformationStack,
    "aws_cloudformation_template": CloudformationTemplate,
    "aws_cloudformation": Cloudformation,
    "aws_cloudtrail": Cloudtrail,
    "aws_cloudwatch_alarm": CloudwatchAlarm,
    "aws_cloudwatch_event_event_based": CloudwatchEventEventBased,
    "aws_cloudwatch_event_time_based": CloudwatchEventTimeBased,
    "aws_cloudwatch_rule": CloudwatchRule,
    "aws_cloudwatch": Cloudwatch,
    "aws_codeguru": Codeguru,
    "aws_cli": CommandLineInterface,
    "aws_config": Config,
    "aws_control_tower": ControlTower,
    "aws_license_manager": LicenseManager,
    "aws_managed_services": ManagedServices,
    "aws_management_governance": ManagementAndGovernance,
    "aws_management_console": ManagementConsole,
    "aws_opsworks_apps": OpsworksApps,
    "aws_opsworks_deployments": OpsworksDeployments,
    "aws_opsworks_instances": OpsworksInstances,
    "aws_opsworks_layers": OpsworksLayers,
    "aws_opsworks_monitoring": OpsworksMonitoring,
    "aws_opsworks_permissions": OpsworksPermissions,
    "aws_opsworks_resources": OpsworksResources,
    "aws_opsworks_stack": OpsworksStack,
    "aws_opsworks": Opsworks,
    "aws_organizations_account": OrganizationsAccount,
    "aws_organizations_organizational_unit": OrganizationsOrganizationalUnit,
    "aws_organizations": Organizations,
    "aws_personal_health_dashboard": PersonalHealthDashboard,
    "aws_proton": Proton,
    "aws_service_catalog": ServiceCatalog,
    "aws_ssm_app_config": SystemsManagerAppConfig,
    "aws_ssm_automation": SystemsManagerAutomation,
    "aws_ssm_documents": SystemsManagerDocuments,
    "aws_ssm_inventory": SystemsManagerInventory,
    "aws_ssm_maintenance_windows": SystemsManagerMaintenanceWindows,
    "aws_ssm_opscenter": SystemsManagerOpscenter,
    "aws_ssm_parameter_store": SystemsManagerParameterStore,
    "aws_ssm_patch_manager": SystemsManagerPatchManager,
    "aws_ssm_run_command": SystemsManagerRunCommand,
    "aws_ssm_state_manager": SystemsManagerStateManager,
    "aws_ssm": SystemsManager,
    "aws_trusted_advisor_checklist_cost": TrustedAdvisorChecklistCost,
    "aws_trusted_advisor_checklist_fault_tolerant": TrustedAdvisorChecklistFaultTolerant,
    "aws_trusted_advisor_checklist_performance": TrustedAdvisorChecklistPerformance,
    "aws_trusted_advisor_checklist_security": TrustedAdvisorChecklistSecurity,
    "aws_trusted_advisor_checklist": TrustedAdvisorChecklist,
    "aws_trusted_advisor": TrustedAdvisor,
    "aws_well_architected_tool": WellArchitectedTool,
    "aws_client": Client,
    "aws_disk": Disk,
    "aws_forums": Forums,
    "aws_general": General,
    "aws_generic_database": GenericDatabase,
    "aws_generic_firewall": GenericFirewall,
    "aws_generic_office_building": GenericOfficeBuilding,
    "aws_generic_saml_token": GenericSamlToken,
    "aws_generic_sdk": GenericSDK,
    "aws_internet_alt_1": InternetAlt1,
    "aws_internet_alt_2": InternetAlt2,
    "aws_marketplace": Marketplace,
    "aws_mobile_client": MobileClient,
    "aws_multimedia": Multimedia,
    "aws_office_building": OfficeBuilding,
    "aws_saml_token": SamlToken,
    "aws_sdk": SDK,
    "aws_ssl_padlock": SslPadlock,
    "aws_tape_storage": TapeStorage,
    "aws_toolkit": Toolkit,
    "aws_traditional_server": TraditionalServer,
    "aws_user": User,
    "aws_users": Users,
    "aws_aurora_instance": AuroraInstance,
    "aws_aurora": Aurora,
    "aws_dms_workflow": DatabaseMigrationServiceDatabaseMigrationWorkflow,
    "aws_dms": DatabaseMigrationService,
    "aws_database": Database,
    "aws_documentdb_mongodb_compatibility": DocumentdbMongodbCompatibility,
    "aws_dynamodb_attribute": DynamodbAttribute,
    "aws_dynamodb_attributes": DynamodbAttributes,
    "aws_dynamodb_dax": DynamodbDax,
    "aws_dynamodb_gsi": DynamodbGlobalSecondaryIndex,
    "aws_dynamodb_item": DynamodbItem,
    "aws_dynamodb_items": DynamodbItems,
    "aws_dynamodb_table": DynamodbTable,
    "aws_dynamodb": Dynamodb,
    "aws_elasticache_cache_node": ElasticacheCacheNode,
    "aws_elasticache_memcached": ElasticacheForMemcached,
    "aws_elasticache_redis": ElasticacheForRedis,
    "aws_elasticache": Elasticache,
    "aws_keyspaces": KeyspacesManagedApacheCassandraService,
    "aws_neptune": Neptune,
    "aws_qldb": QuantumLedgerDatabaseQldb,
    "aws_rds_instance": RDSInstance,
    "aws_rds_mariadb": RDSMariadbInstance,
    "aws_rds_mysql": RDSMysqlInstance,
    "aws_rds_on_vmware": RDSOnVmware,
    "aws_rds_oracle": RDSOracleInstance,
    "aws_rds_postgresql": RDSPostgresqlInstance,
    "aws_rds_sql_server": RDSSqlServerInstance,
    "aws_rds": RDS,
    "aws_redshift_dense_compute_node": RedshiftDenseComputeNode,
    "aws_redshift_dense_storage_node": RedshiftDenseStorageNode,
    "aws_redshift": Redshift,
    "aws_timestream": Timestream,
    "aws_api_gateway_endpoint": APIGatewayEndpoint,
    "aws_api_gateway": APIGateway,
    "aws_app_mesh": AppMesh,
    "aws_client_vpn": ClientVpn,
    "aws_cloud_map": CloudMap,
    "aws_cloudfront_download_distribution": CloudFrontDownloadDistribution,
    "aws_cloudfront_edge_location": CloudFrontEdgeLocation,
    "aws_cloudfront_streaming_distribution": CloudFrontStreamingDistribution,
    "aws_cloudfront": CloudFront,
    "aws_direct_connect": DirectConnect,
    "aws_elastic_load_balancing": ElasticLoadBalancing,
    "aws_elb_application_load_balancer": ElbApplicationLoadBalancer,
    "aws_elb_classic_load_balancer": ElbClassicLoadBalancer,
    "aws_elb_network_load_balancer": ElbNetworkLoadBalancer,
    "aws_endpoint": Endpoint,
    "aws_global_accelerator": GlobalAccelerator,
    "aws_internet_gateway": InternetGateway,
    "aws_nacl": Nacl,
    "aws_nat_gateway": NATGateway,
    "aws_network_firewall": NetworkFirewall,
    "aws_networking_content_delivery": NetworkingAndContentDelivery,
    "aws_subnet.private": PrivateSubnet,
    "aws_privatelink": Privatelink,
    "aws_subnet.public": PublicSubnet,
    "aws_route53_hosted_zone": Route53HostedZone,
    "aws_route53": Route53,
    "aws_route_table": RouteTable,
    "aws_site_to_site_vpn": SiteToSiteVpn,
    "aws_transit_gateway": TransitGateway,
    "aws_vpc_customer_gateway": VPCCustomerGateway,
    "aws_vpc_elastic_network_adapter": VPCElasticNetworkAdapter,
    "aws_vpc_elastic_network_interface": VPCElasticNetworkInterface,
    "aws_vpc_flow_logs": VPCFlowLogs,
    "aws_vpc_peering": VPCPeering,
    "aws_vpc_router": VPCRouter,
    "aws_vpc_traffic_mirroring": VPCTrafficMirroring,
    "aws_vpc": VPC,
    "aws_vpn_connection": VpnConnection,
    "aws_vpn_gateway": VpnGateway,
    "aws_apprunner_service": AppRunner,
    "aws_autoscaling_group": ApplicationAutoScaling,
    "aws_batch_compute_environment": Batch,
    "aws_batch_job_definition": Batch,
    "aws_batch_job_queue": Batch,
    "aws_compute_optimizer": ComputeOptimizer,
    "aws_compute_instance": Compute,
    "aws_ami": EC2Ami,
    "aws_autoscaling_policy": EC2AutoScaling,
    "aws_ecr_image": EC2ContainerRegistryImage,
    "aws_ecr_repository": EC2ContainerRegistry,
    "aws_ecr_registry": EC2ContainerRegistryRegistry,
    "aws_elastic_ip": EC2ElasticIpAddress,
    "aws_imagebuilder_pipeline": EC2ImageBuilder,
    "aws_instance": EC2Instance,
    "aws_instances": EC2Instances,
    "aws_rescue": EC2Rescue,
    "aws_spot_instance": EC2SpotInstance,
    "aws_ec2": EC2,
    "aws_elastic_beanstalk_environment": ElasticBeanstalkApplication,
    "aws_elastic_beanstalk_deployment": ElasticBeanstalkDeployment,
    "aws_elastic_beanstalk": ElasticBeanstalk,
    "aws_ecs_container": ElasticContainerServiceContainer,
    "aws_ecs_service": ElasticContainerServiceService,
    "aws_ecs": ElasticContainerService,
    "aws_eks_cluster": ElasticKubernetesService,
    "aws_fargate_profile": Fargate,
    "aws_lambda_function": LambdaFunction,
    "aws_lambda": Lambda,
    "aws_lightsail_instance": Lightsail,
    "aws_local_zones": LocalZones,
    "aws_outposts_instance": Outposts,
    "aws_serverless_repo": ServerlessApplicationRepository,
    "aws_thinkbox_deadline": ThinkboxDeadline,
    "aws_thinkbox_draft": ThinkboxDraft,
    "aws_thinkbox_frost": ThinkboxFrost,
    "aws_thinkbox_krakatoa": ThinkboxKrakatoa,
    "aws_thinkbox_sequoia": ThinkboxSequoia,
    "aws_thinkbox_stoke": ThinkboxStoke,
    "aws_thinkbox_xmesh": ThinkboxXmesh,
    "aws_vmware_cloud_on_aws": VmwareCloudOnAWS,
    "aws_wavelength_zone": Wavelength,
    "aws_opensearch_service": AmazonOpensearchService,
    "aws_analytics": Analytics,
    "aws_athena": Athena,
    "aws_cloudsearch_search_documents": CloudsearchSearchDocuments,
    "aws_cloudsearch": Cloudsearch,
    "aws_data_lake_resource": DataLakeResource,
    "aws_data_pipeline": DataPipeline,
    "aws_elasticsearch_service": ElasticsearchService,
    "aws_emr_cluster": EMRCluster,
    "aws_emr_engine_mapr_m3": EMREngineMaprM3,
    "aws_emr_engine_mapr_m5": EMREngineMaprM5,
    "aws_emr_engine_mapr_m7": EMREngineMaprM7,
    "aws_emr_engine": EMREngine,
    "aws_emr_hdfs_cluster": EMRHdfsCluster,
    "aws_emr": EMR,
    "aws_glue_crawlers": GlueCrawlers,
    "aws_glue_data_catalog": GlueDataCatalog,
    "aws_glue": Glue,
    "aws_kinesis_data_analytics": KinesisDataAnalytics,
    "aws_kinesis_data_firehose": KinesisDataFirehose,
    "aws_kinesis_data_streams": KinesisDataStreams,
    "aws_kinesis_video_streams": KinesisVideoStreams,
    "aws_kinesis": Kinesis,
    "aws_lake_formation": LakeFormation,
    "aws_managed_streaming_for_kafka": ManagedStreamingForKafka,
    "aws_quicksight": Quicksight,
}

default_icon = General


def parse_dot_to_diagram(directory: str, output_file="terraform_graph"):
    dot_data = ''.join(readfile(directory))
    dot_graph = pydot.graph_from_dot_data(dot_data)[0]

    graph_attributes = {
        "bgcolor": "#000021",
        "rankdir": "RL",
        "nodesep": "2.0",
        "ranksep": "2.5",
        "fontsize": "10",
    }

    node_attributes = {
        "shape": "box",
        "fontsize": "20",
        "width": "0.0",
        "height": "0.0",
        "fixedsize": "false",
        "style": "rounded",
        "fontcolor": "white",
        "labelloc": "b",
    }

    with Diagram(
        output_file, show=False, graph_attr=graph_attributes, node_attr=node_attributes
    ):
        created_nodes = {}

        # Create nodes
        for node in dot_graph.get_nodes():
            node_name = node.get_name().strip('"')
            label = node.get_label().strip('"') if node.get_label() else node_name
            resource_type0 = node_name
            resource_type1 = node_name.split(".")[0]
            node_icon = (
                resource_icon_map.get(resource_type0)
                or resource_icon_map.get(resource_type1)
                or default_icon
            )
            created_nodes[node_name] = node_icon(label)

        # Create edges
        for edge in dot_graph.get_edges():
            src = edge.get_source().strip('"')
            dest = edge.get_destination().strip('"')
            if src in created_nodes and dest in created_nodes:
                created_nodes[src] >> created_nodes[dest]

    upload_image(".".join([output_file, "png"]), "session_id")