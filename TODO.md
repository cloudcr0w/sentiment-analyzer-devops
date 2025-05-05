# Project TODO – Sentiment Analyzer DevOps

This file tracks pending tasks and development goals for the project.

## Completed
- FastAPI backend initialized
- Dockerfile created (base image: python:3.10-bookworm)
- Terraform config for EC2 with security group
- Ansible provisioning playbook (deploy.yml)
- App deployed to EC2 via Ansible

## In Progress / Planned

### Infrastructure (Terraform)
- Output EC2 public IP
- Optional: S3 bucket for model storage
- Parameterize AMI ID and tags

### Provisioning (Ansible)
- Convert uvicorn to systemd service
- Add .env handling
- Optional: Install and configure nginx for reverse proxy

### Application (FastAPI)
- Add API key validation logic
- Load model and vectorizer from file
- Validate input and improve error handling

### Local Development
- Add docker-compose.yml for testing
- Add Makefile with basic targets (build, run, deploy)

### Security
- Add middleware for API key authorization
- Add basic rate limiting or throttling
- Optional: Add WAF or API Gateway (future work)

### Documentation
- terraform/README.md with usage instructions
- ansible/README.md with setup and SSH guide
- Architecture diagram (EC2, Ansible, FastAPI)
