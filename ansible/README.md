# Ansible – EC2 Provisioning for Sentiment Analyzer

This playbook installs required packages and deploys the FastAPI app on an EC2 instance.

## 🔧 What it does

- Installs Python, pip, Git
- Clones the GitHub repository
- Installs app dependencies
- Copies model files (`model.pkl`, `vectorizer.pkl`)
- Starts the FastAPI app on port 8000

## ▶️ Usage

1. Run `terraform apply` in the `terraform/` directory.

2. After apply, copy the EC2 public IP from Terraform output:
   ```bash
   terraform output ec2_public_ip
   ```

3. Paste that IP into ansible/hosts like this:

[all]
44.203.xx.xx

4. Run the playbook:

```bash
ansible-playbook -i hosts deploy.yml --private-key ~/keys/crowKeyPairV2.pem -u ubuntu
```

✅ Make sure your .pem key is in place
✅ Port 22 is open (check Security Group)
✅ The EC2 instance is running