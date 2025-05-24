# Review Guide

## Quick Start

1. Provision infrastructure:
   ```bash
   terraform apply
```

2. Deploy app:
```bash
ansible-playbook -i hosts deploy.yml
```
3. Check:

http://<your-ec2-ip>:8000/health

Swagger at /docs

Key Features
Model pulled from S3

Systemd service

Real-world provisioning

