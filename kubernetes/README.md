# ☸️ Kubernetes – Sentiment Analyzer

Kubernetes manifests to deploy the FastAPI-based sentiment analyzer.

## 📄 Files

- `deployment.yml` – Deploys 1 replica on port 8000
- `service.yml` – Exposes app via LoadBalancer on port 80

## 🚀 Usage

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl get svc sentiment-analyzer-service
```

App should be accessible at http://<EXTERNAL-IP>/docs

## 📌 Notes
Uses sentiment-analyzer:latest – update to full image path for real use

Optional: add .env, probes, and resource limits later