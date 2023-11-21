provider "aws" {
  region = "us-east-1"  # Set your AWS region
}

resource "aws_s3_bucket" "input_bucket" {
  bucket = "your-input-bucket-name"
  acl    = "private"
  # Add other bucket configurations as needed
}

resource "aws_s3_bucket" "output_bucket" {
  bucket = "your-output-bucket-name"
  acl    = "private"
  # Add other bucket configurations as needed
}

resource "null_resource" "create_transform_job" {
  triggers = {
    always_run = "${timestamp()}"
  }

  provisioner "local-exec" {
    command = <<-EOT
      python3 "${path.module}/create_sagemaker_transform_job.py" \
        "your-transform-job-name" \
        "your-sagemaker-model-name" \
        "s3://${aws_s3_bucket.input_bucket.bucket}/input-prefix/" \
        "s3://${aws_s3_bucket.output_bucket.bucket}/output-prefix/" \
        "ml.m5.large" \
        1
    EOT
  }
}
