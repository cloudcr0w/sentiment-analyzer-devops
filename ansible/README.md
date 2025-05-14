# Ansible – EC2 Provisioning for Sentiment Analyzer

This playbook installs required packages and deploys the FastAPI app on an EC2 instance.

## What it does

- Installs Python, pip, Git
- Clones the GitHub repository
- Installs app dependencies
- Copies model files (`model.pkl`, `vectorizer.pkl`)
- Starts the FastAPI app

## Usage

```bash
ansible-playbook -i hosts ansible/deploy.yml
```

Make sure:

Your SSH key is configured

The EC2 instance is reachable (public IP, port 22 open)

## What it does
Installs Python, pip, git

Clones the repo

Installs dependencies

Starts the FastAPI app on port 8000