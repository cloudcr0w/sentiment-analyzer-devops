.PHONY: init plan apply deploy

init:
	cd terraform && terraform init

plan:
	cd terraform && terraform plan

apply:
	cd terraform && terraform apply

deploy:
	ansible-playbook -i hosts ansible/deploy.yml
