variable "aws_region" {
  description = "AWS region to deploy to"
  type        = string
  default     = "us-east-1"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"
}

variable "key_name" {
  description = "EC2 Key Pair name for SSH access"
  type        = string
}
variable "ami_id" {
  description = "AMI ID for the EC2 instance"
  type        = string
}

variable "instance_name" {
  description = "Name tag for the EC2 instance"
  type        = string
  default     = "SentimentAnalyzer"
}

variable "environment" {
  type    = string
  default = "dev"
}
variable "my_ip_cidr" {
  description = "Your IP address in CIDR notation (e.g. 1.2.3.4/32)"
  type        = string
}