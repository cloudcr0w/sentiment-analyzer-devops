# Terraform configuration for sentiment-analyzer infrastructure
# Planned:
# - AWS provider
# - EC2 instance with public IP
# - Security Group for FastAPI (port 8000)
provider "aws" {
  region = var.aws_region
}

resource "aws_security_group" "fastapi_sg" {
  name        = "fastapi-sg"
  description = "Allow inbound access to FastAPI and SSH"

  ingress {
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = [var.my_ip_cidr]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.my_ip_cidr]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name        = "SentimentAnalyzerSG"
    Environment = var.environment
  }
}

resource "aws_instance" "fastapi_server" {
  ami                         = var.ami_id
  instance_type               = var.instance_type
  key_name                    = var.key_name
  vpc_security_group_ids      = [aws_security_group.fastapi_sg.id]
  associate_public_ip_address = true

  tags = {
    Name = var.instance_name
  }
}
