# 🧠 Project TODO – Sentiment Analyzer DevOps

This file tracks development goals and remaining tasks.

---

## ✅ Completed

- **FastAPI backend** initialized (`main.py`)
- **Machine Learning model** trained (Naive Bayes + CountVectorizer)
- Endpoints: `/predict`, `/health`, `/version`, `/logs`
- **Input validation** with Pydantic (`min_length`)
- **Auth & Security**:
  - API key auth via `.env`
  - Rate limiting by IP (custom middleware)
  - Logging to `security.log`
- **Infrastructure**:
  - Terraform: EC2 + SG + S3 bucket + outputs
  - Ansible: provisioning, model download from S3, systemd deploy
- **Containers**:
  - Dockerfile created (Python 3.10, Debian Bookworm)
  - Docker Compose for local dev
- **Kubernetes** manifests: `deployment.yaml`, `service.yaml`
- **Tooling**:
  - Makefile with `run-local`, `lint`
  - Directory structure cleaned (`__init__.py`, `env.example`)
- **Docs**:
  - Project diagram
  - Split `README.md` and `REVIEW_GUIDE.md`
  - `app/` marked as Python package

---

## 🔧 Still To Do

### 📦 Infrastructure (Terraform)
- (Optional) Add **remote backend** (S3 + DynamoDB for state locking)
- (Optional) Add **API Gateway** or ALB for secure API exposure

### ⚙️ CI/CD & Automation
- Add **GitHub Actions workflow** (build → lint → test → deploy)
- Extend **Makefile**: `build`, `docker-run`, `compose-up`

### 🔐 Security / Hardening
- Dockerfile: switch to **non-root user**
- Store secrets in **Kubernetes Secret** or **AWS SSM**

### 📈 Monitoring / Observability
- Add `/metrics` endpoint (Prometheus format)
- Collect request counts, latency, error rates
- (Optional) Dashboard in **Grafana** / CloudWatch

### 📦 Packaging & Delivery
- Publish Docker image to **DockerHub** (or AWS ECR)
- Kubernetes: replace hardcoded envs with **ConfigMap** + **Secret**

### 🧪 Tests
- Unit test for `/predict` with pytest
- Add coverage badge to repo

---

## 📝 Notes

This project demonstrates a **cloud-native DevOps workflow**:  
- Infrastructure as Code (Terraform + Ansible)  
- Containerization & Orchestration (Docker, Kubernetes)  
- Security-first design (auth, rate limiting, logging)  
- CI/CD readiness (GitHub Actions planned)  

👉 Use `REVIEW_GUIDE.md` for deployment instructions and `docker-compose.yml` for local testing.
