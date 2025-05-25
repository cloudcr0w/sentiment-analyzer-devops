# Project TODO – Sentiment Analyzer DevOps

This file tracks development goals and remaining tasks.

## ✅ Completed
- FastAPI backend initialized
- Dockerfile created (base image: python:3.10-bookworm)
- Trained and saved basic ML model (Naive Bayes + CountVectorizer)
- Connected model to `/predict` endpoint
- `/health` endpoint added
- Terraform: EC2 instance, security group, S3 bucket, outputs
- Ansible: provisioning with app clone, pip install, `.env` injection
- Model files pulled from S3 in Ansible
- FastAPI runs as systemd service
- README split: main + REVIEW_GUIDE
- Added Makefile
- Kubernetes manifests with usage doc
- Diagram added to main README

## 🛠️ Still To Do

### Infrastructure (Terraform)
- (Optional) Use remote backend (S3 + DynamoDB)

### Application (FastAPI)
- Add API key middleware ✅ (planned/ready)
- Add basic rate limiting (e.g. per IP)
- Improve input validation & error responses
- Add `/metrics` endpoint or Prometheus logging

### Local Dev / CI
- Add `docker-compose.yml` for local dev (optional)
- Extend Makefile: `run-local`, `test`, `lint`
- Add CI/CD GitHub Actions workflow (build + lint)

### Security / Hardening
- Add logging of abuse attempts to `security.log`
- Restrict CORS / IPs in FastAPI
- Dockerfile hardening (no root user)
- (Optional) Add WAF or deploy via API Gateway

