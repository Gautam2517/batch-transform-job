import boto3

# Replace these values with your actual information
s3_input_path = 's3://data-science--bucket/Churn-Model-Data/test.csv'
s3_output_path = 's3://data-science--bucket/Churn-Model-Data/predictions.csv'
model_name = 'pipelines-emjhj52r2i60-CreateModel-uaSTQQCHqS'
instance_type = 'ml.m5.large'
job_name = 'trail_job'

# Specify AWS credentials
aws_access_key_id = 'AKIAYFSXQ23HHOFCROMV'
aws_secret_access_key = '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'
aws_region = 'us-east-1'

# Create a SageMaker client with specified credentials
sagemaker = boto3.client('sagemaker',
                        aws_access_key_id=aws_access_key_id,
                        aws_secret_access_key=aws_secret_access_key,
                        region_name=aws_region)

# Specify the input configuration
transform_input = {
    'DataSource': {
        'S3DataSource': {
            'S3DataType': 'S3Prefix',
            'S3Uri': s3_input_path
        }
    },
    'ContentType': 'text/csv',
    'SplitType': 'Line',
}

# Specify the output configuration
transform_output = {
    'S3OutputPath': s3_output_path,
}

# Specify the parameters for the Batch Transform job
transform_job_params = {
    'TransformJobName': 'trail-job',  # Use quotes around the job name
    'ModelName': model_name,
    'MaxConcurrentTransforms': 1,
    'MaxPayloadInMB': 6,
    'BatchStrategy': 'MultiRecord',
    'TransformInput': transform_input,
    'TransformOutput': transform_output,
    'TransformResources': {
        'InstanceType': instance_type,
        'InstanceCount': 1,
    }
}

# Create the Batch Transform job
sagemaker.create_transform_job(**transform_job_params)

print(f"Batch Transform job '{job_name}' created successfully.")

