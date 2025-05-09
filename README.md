A minimal sentiment analysis API built with FastAPI and scikit-learn. 
This project demonstrates how to wrap a simple ML model in a containerized REST API, ready for deployment in AWS or Kubernetes.

## Project Structure

- `app/` – FastAPI app and dependencies
- `model/` – ML training script and artifacts
- `terraform/` – AWS infrastructure as code
- `ansible/` – server provisioning (Docker, app deployment)
- `kubernetes/` – deployment YAMLs for K8s
- `security/` – checklists and API protection logic

##  Secure-by-Design API Architecture

This FastAPI-based NLP service implements basic security layers to protect against common API threats:

- **Token-based Authentication** (via `Authorization: Bearer <token>`)
- **Rate Limiting** (max 5 requests per minute per IP)
- **Abuse Logging** (unauthorized access, flood attempts)
- **Dockerized for reproducibility and Kubernetes-ready**

These mechanisms demonstrate foundational API protection practices and can be extended for OAuth2, JWT, or third-party auth providers.

## Security Features
- `Authorization: Bearer <token>` required for `/predict`
- Rate limiting: max 5 requests per minute per IP
- Logs unauthorized access and abuse attempts to `security.log`
