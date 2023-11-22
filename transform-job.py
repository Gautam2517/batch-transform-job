import boto3

# Replace these values with your actual information
s3_input_path = 's3://data-science--bucket/Churn-Model-Data/test.csv'
s3_output_path = 's3://data-science--bucket/Churn-Model-Data/predictions.csv'
model_name = 'rf_model'
instance_type = 'ml.m5.large'
job_name = 'trail-job'

# Create a SageMaker client
sagemaker = boto3.client('sagemaker')

# Specify the input configuration
transform_input = {
    'DataSource': {
        'S3DataSource': {
            'S3DataType': 'S3Prefix',
            'S3Uri': 's3://data-science--bucket/Churn-Model-Data/test.csv'
        }
    },
    'ContentType': 'text/csv',
    'SplitType': 'Line',
}

# Specify the output configuration
transform_output = {
    'S3OutputPath': 's3://data-science--bucket/Churn-Model-Data/predictions.csv'
}

# Specify the parameters for the Batch Transform job
transform_job_params = {
    'TransformJobName': trail-job,
    'ModelName': rf_model,
    'MaxConcurrentTransforms': 1,
    'MaxPayloadInMB': 6,
    'BatchStrategy': 'MultiRecord',
    'TransformInput': 's3://data-science--bucket/Churn-Model-Data/test.csv',
    'TransformOutput': 's3://data-science--bucket/Churn-Model-Data/predictions.csv',
    'TransformResources': {
        'InstanceType': ml.m5.large,
        'InstanceCount': 1,
    }
}

# Create the Batch Transform job
sagemaker.create_transform_job(**transform_job_params)

print(f"Batch Transform job '{job_name}' created successfully.")

