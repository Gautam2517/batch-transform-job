# your_script.py

import os
#from dotenv import load_dotenv
import boto3

# Load environment variables from .env file
#load_dotenv()

# from dotenv import load_dotenv
import boto3

# Load environment variables from .env file
# load_dotenv()

# Access environment variables
S3_INPUT_PATH = os.getenv("S3_INPUT_PATH")
print(S3_INPUT_PATH)

#S3_OUTPUT_PATH = os.getenv("S3_OUTPUT_PATH")
#MODEL_NAME = os.getenv("MODEL_NAME")
#INSTANCE_TYPE = os.getenv("INSTANCE_TYPE")
#JOB_NAME = os.getenv("JOB_NAME")

# Create an S3 client
s3 = boto3.client('s3')

# Specify the input configuration
transform_input = {
    'DataSource': {
        'S3DataSource': {
            'S3DataType': 'S3Prefix',
            'S3Uri': S3_INPUT_PATH
        }
    },
    'ContentType': 'text/csv',
    'SplitType': 'Line',
}

# Specify the output configuration
#transform_output = {
 #   'S3OutputPath': S3_OUTPUT_PATH,
#}

# Specify the parameters for the Batch Transform job
#transform_job_params = {
 #   'TransformJobName': JOB_NAME,
  #  'ModelName': MODEL_NAME,
   # 'MaxConcurrentTransforms': 1,
    #'MaxPayloadInMB': 6,
    #'BatchStrategy': 'MultiRecord',
    #'TransformInput': transform_input,
    #'TransformOutput': transform_output,
    #'TransformResources': {
     #   'InstanceType': INSTANCE_TYPE,
      #  'InstanceCount': 1,
    #}
#}

# Create the Batch Transform job
#sagemaker = boto3.client('sagemaker')
#sagemaker.create_transform_job(**transform_job_params)

# Customize the success message or add additional logic here
#print(f"Batch Transform job '{JOB_NAME}' created successfully.")
# S3_OUTPUT_PATH = os.getenv("S3_OUTPUT_PATH")
# MODEL_NAME = os.getenv("MODEL_NAME")
# INSTANCE_TYPE = os.getenv("INSTANCE_TYPE")
# JOB_NAME = os.getenv("JOB_NAME")

# # Create an S3 client
# s3 = boto3.client('s3')

# # Specify the input configuration
# transform_input = {
#     'DataSource': {
#         'S3DataSource': {
#             'S3DataType': 'S3Prefix',
#             'S3Uri': S3_INPUT_PATH
#         }
#     },
#     'ContentType': 'text/csv',
#     'SplitType': 'Line',
# }

# # Specify the output configuration
# transform_output = {
#     'S3OutputPath': S3_OUTPUT_PATH,
# }

# # Specify the parameters for the Batch Transform job
# transform_job_params = {
#     'TransformJobName': JOB_NAME,
#     'ModelName': MODEL_NAME,
#     'MaxConcurrentTransforms': 1,
#     'MaxPayloadInMB': 6,
#     'BatchStrategy': 'MultiRecord',
#     'TransformInput': transform_input,
#     'TransformOutput': transform_output,
#     'TransformResources': {
#         'InstanceType': INSTANCE_TYPE,
#         'InstanceCount': 1,
#     }
# }

# # Create the Batch Transform job
# sagemaker = boto3.client('sagemaker')
# sagemaker.create_transform_job(**transform_job_params)

# # Customize the success message or add additional logic here
# print(f"Batch Transform job '{JOB_NAME}' created successfully.")


