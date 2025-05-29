# 🧠 Project TODO – Sentiment Analyzer DevOps

This file tracks development goals and remaining tasks.

---

## ✅ Completed

- FastAPI backend initialized (`main.py`)
- Dockerfile created (Python 3.10, Bookworm)
- ML model trained (Naive Bayes + CountVectorizer)
- `/predict` and `/health` endpoints added
- Input validation with Pydantic (`min_length`)
- API key auth via `.env`
- Rate limiting by IP (custom middleware)
- Logging to `security.log`
- Terraform: EC2 + SG + S3 bucket + outputs
- Ansible: provisioning, model download from S3, systemd deploy
- Docker Compose for local dev
- Kubernetes manifests (`deployment.yaml`, `service.yaml`)
- Added `/version` and `/logs` endpoints
- Project diagram + split README and REVIEW_GUIDE
- Added Makefile with `run-local`, `lint`
- Directory structure cleaned (`__init__.py`, `env.example`)
- `app/` marked as Python package

---

## 🔧 Still To Do

### 📦 Infrastructure (Terraform)
- (Optional) Add remote backend with S3 + DynamoDB state locking

### ⚙️ CI/CD & Automation
- Add GitHub Actions workflow (build, lint, test)
- Add Makefile: `build`, `docker-run`, `compose-up`

### 🔐 Security / Hardening
- Dockerfile: switch to non-root user
- (Optional) Add WAF or expose API via AWS API Gateway

### 📈 Monitoring / Observability
- Add `/metrics` endpoint or Prometheus integration
- Log request counts / stats

### 📦 Packaging & Delivery
- Publish image to DockerHub (or ECR)
- Use `ConfigMap` / `Secret` in Kubernetes for API_KEY

### 🧪 Tests (optional)
- Add unit test for `/predict`
- Integrate with pytest / coverage

---

## 📝 Notes

This is an MVP-level fullstack DevOps project showing IaC, security, CI readiness and cloud-native packaging.  
Use `REVIEW_GUIDE.md` to deploy end-to-end and `docker-compose.yml` for quick local testing.
