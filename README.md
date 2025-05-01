A minimal sentiment analysis API built with FastAPI and scikit-learn. 
This project demonstrates how to wrap a simple ML model in a containerized REST API, ready for deployment in AWS or Kubernetes.

## Project Structure

- `app/` – FastAPI app and dependencies
- `model/` – ML training script and artifacts
- `terraform/` – AWS infrastructure as code
- `ansible/` – server provisioning (Docker, app deployment)
- `kubernetes/` – deployment YAMLs for K8s
- `security/` – checklists and API protection logic
