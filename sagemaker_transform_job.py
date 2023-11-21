import boto3
import sys

transform_job_name = sys.argv[1]
model_name = sys.argv[2]
input_s3_uri = sys.argv[3]
output_s3_uri = sys.argv[4]
instance_type = sys.argv[5]
instance_count = int(sys.argv[6])

sagemaker_client = boto3.client("sagemaker", region_name="your-region")

transform_input = {
    "DataSource": {
        "S3DataSource": {
            "S3DataType": "S3Prefix",
            "S3Uri": input_s3_uri
        }
    }
}

transform_output = {
    "S3OutputPath": output_s3_uri
}

transform_resources = {
    "InstanceType": instance_type,
    "InstanceCount": instance_count
}

response = sagemaker_client.create_transform_job(
    TransformJobName=transform_job_name,
    ModelName=model_name,
    TransformInput=transform_input,
    TransformOutput=transform_output,
    TransformResources=transform_resources
)

print(f"Transform Job ARN: {response['TransformJobArn']}")

