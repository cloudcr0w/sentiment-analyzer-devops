# 🧠 Sentiment Analyzer – ML API with FastAPI

![Visitors](https://visitor-badge.laobi.icu/badge?page_id=cloudcr0w.sentiment-analyzer-devops)
![K8s Ready](https://img.shields.io/badge/Kubernetes-Ready-blue?logo=kubernetes)


Minimal REST API for sentiment analysis using **FastAPI** + **scikit-learn**.  
Infra via **Terraform** (EC2) + **Ansible** (provisioning). Secure and cloud-ready.

## ▶️ Stack

- `FastAPI` + `uvicorn`
- `scikit-learn` (Naive Bayes)
- `Terraform` – AWS EC2, SG
- `Ansible` – installs & deploys app
- `Docker` – optional container
- `Kubernetes` – deployment manifests

## ✅ Project Structure

```bash
app/         → FastAPI app code
model/       → Trained model + vectorizer
terraform/   → AWS IaC (EC2, SG)
ansible/     → App provisioning (Python, Git, start app)
kubernetes/  → Deployment YAMLs for K8s (optional)
security/    → Auth, rate limiting, logging
```

![Deployment Diagram](./sentiment-diagram.png)

## 🔍 For Reviewers
This project demonstrates:

✅ Infrastructure as Code (Terraform – EC2, S3)
✅ Provisioning with Ansible (app deploy, model from S3)
✅ ML API (FastAPI + Naive Bayes)
✅ Deployment-ready structure with systemd service
✅ GitHub Actions planned for CI/CD

🧪 Full deployment & usage: REVIEW_GUIDE.md

Reach out if you’d like a full demo or want to discuss implementation.

👨‍💻 About the Author
Created by Adam Wrona as part of his DevOps & Cloud Engineering journey 🚀
I'm open to feedback, improvements and contributions — feel free to fork or reach out!

> Reach out if you’d like a full demo or want to discuss implementation.


## 👨‍💻 About the Author
Created by Adam Wrona as part of his DevOps & Cloud Engineering journey 🚀
I'm open to feedback, improvements and contributions — feel free to fork or reach out!

## 💡 Like this project?

⭐ Star it on GitHub

🍴 Fork it

🧠 Share your ideas in Issues/Discussions

```diff
+ “99% of debugging is staring at the screen in disbelief.”
+ „99% debugowania to patrzenie w ekran z niedowierzaniem.”
+ — prawie prawda™
```
