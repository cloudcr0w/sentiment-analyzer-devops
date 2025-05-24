# Review Guide

## Quick Start

## 🧱 Deploy Flow

🚀 DevOps Usage

### 1. Deploy infrastructure
```bash
cd terraform
terraform apply
```

### 2. Copy EC2 IP from terraform output to ansible/hosts

```bash
 Example:
 [ec2]
 44.203.XX.XX ansible_user=ubuntu ansible_ssh_private_key_file=~/keys/crowKeyPairV2.pem
```

### 3. Run Ansible playbook

```bash
cd ../ansible
ansible-playbook -i hosts deploy.yml
```

## 🌐 Access API

Swagger UI: http://<EC2_IP>:8000/docs

POST to /predict with JSON body:

```json

{
  "text": "Awesome project!"
}
```

And header:

Authorization: Bearer your-token

for example :
```bash
curl -X POST http://<EC2_IP>:8000/predict \
  -H "Authorization: Bearer your-token" \
  -H "Content-Type: application/json" \
  -d '{"text": "Awesome project!"}'
```

---
🧪 Try it out:
- `curl http://<your-ec2-ip>:8000/health`
- Swagger UI: `http://<your-ec2-ip>:8000/docs`
- or run it locally via Docker/Ansible