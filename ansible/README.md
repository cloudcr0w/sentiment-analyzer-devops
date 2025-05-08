# Ansible Provisioning

This playbook will be used to:
- Set up Docker on EC2 instance
- Pull the Docker image
- Run the FastAPI container
- Ensure idempotency and reusability

Host: AWS EC2 (Ubuntu)

## Usage

```bash
ansible-playbook -i hosts ansible/deploy.yml
```

Make sure the instance is reachable via SSH and your SSH key is configured.

What it does
Installs Python, pip, git

Clones the repo

Installs dependencies

Starts the FastAPI app on port 8000