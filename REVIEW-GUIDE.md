# Review Guide

End-to-end deployment & testing instructions for **Sentiment Analyzer DevOps**.

---

## 🧱 Deploy Flow (Cloud)

### 1. Provision infrastructure (Terraform)
```bash
cd terraform
terraform init
terraform apply
```
Outputs will include the EC2 public IP.


### 2. Configure Ansible inventory

Copy the EC2 IP from Terraform output into ansible/hosts:
```bash
[ec2]
44.203.XX.XX ansible_user=ubuntu ansible_ssh_private_key_file=~/keys/crowKeyPairV2.pem
```

### 3. Run Ansible playbook
```bash
cd ../ansible
ansible-playbook -i hosts deploy.yml
```

### This will:

install dependencies

download ML model from S3

configure systemd service

start API backend

### 🧪 Local Testing

Run locally with Docker Compose:
```bash
docker-compose up --build
```
or via Makefile shortcut:
```bash
or via Makefile shortcut:
```

Then access:

Healthcheck → http://localhost:8000/health

Docs (Swagger UI) → http://localhost:8000/docs

### 🌐 Access Deployed API

Swagger UI:
```bash
http://<EC2_IP>:8000/docs
```

Health check:
```bash
curl http://<EC2_IP>:8000/health
```

Prediction example (with API key):
```bash

export API_KEY="your-token"

curl -X POST http://<EC2_IP>:8000/predict \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"text": "Awesome project!"}'
```

### 📝 Notes

Replace <EC2_IP> with the public IP from Terraform outputs.

Ansible requires SSH access (key must match the Terraform EC2 keypair).

Logs are stored in security.log on the server.

Local vs Cloud behavior is the same (same Docker image).