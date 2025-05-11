# Project TODO – Sentiment Analyzer DevOps

This file tracks pending tasks and development goals for the project.

## Completed
- FastAPI backend initialized
- Dockerfile created (base image: python:3.10-bookworm)
- Trained and saved basic ML model (Naive Bayes + CountVectorizer)
- Connected model to `/predict` endpoint
- Successfully tested prediction via Swagger UI (/docs)
- `/health` endpoint added
- Terraform setup: EC2 instance, security group, variables and output
- Ansible playbook provisioning EC2 instance and deploying app
- Added Makefile for simplified CLI automation
- Added documentation for Terraform and Ansible directories

## In Progress / Planned

### Infrastructure (Terraform)
- Optional: S3 bucket for model storage
- Optional: Use remote backend (e.g. S3 + DynamoDB for state locking)

### Provisioning (Ansible)
- Copy `model.pkl` and `vectorizer.pkl` to EC2 during provisioning
- Convert `uvicorn` background task to `systemd` service
- Add support for `.env` injection
- Optional: Install and configure nginx as reverse proxy

### Application (FastAPI)
- Add API key validation logic (e.g. via `Header` or middleware)
- Improve input validation and error handling
- Add `/metrics` or logging for request statistics

### Local Development
- Add `docker-compose.yml` for local testing
- Expand Makefile with more commands (e.g., `test`, `lint`, `run-local`)

### Security
- Add middleware for API key authorization
- Add basic rate limiting (e.g., via IP)
- Optional: Add WAF or expose via AWS API Gateway

### Documentation
- Add architecture diagram (EC2, FastAPI, Ansible, Terraform, model)
- Add usage examples to project-level README
