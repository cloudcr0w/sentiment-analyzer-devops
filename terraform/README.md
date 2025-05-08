# Terraform – Sentiment Analyzer Infrastructure

This directory contains Terraform configuration to deploy an EC2 instance on AWS for hosting the FastAPI sentiment analysis app.

## Requirements
- AWS CLI configured (`aws configure`)
- Terraform installed (`terraform -v`)
- Existing EC2 Key Pair name

## Setup

1. Edit `terraform.tfvars`:

```hcl
aws_region    = "us-east-1"
instance_type = "t2.micro"
key_name      = "your-keypair-name"
ami_id        = "ami-0c02fb55956c7d316"  # Amazon Linux 2
instance_name = "SentimentAnalyzer"

2. Initialize and apply:

```bash
terraform init
terraform plan
terraform apply
```

3. Output:

After applying, the public IP of the EC2 instance will be displayed.

Notes
Do not commit terraform.tfvars.

Output includes the EC2 public IP for use with Ansible or browser access.
