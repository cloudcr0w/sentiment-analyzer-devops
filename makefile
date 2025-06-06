.PHONY: init plan apply deploy run-local lint build compose-up

init:
	cd terraform && terraform init

plan:
	cd terraform && terraform plan

apply:
	cd terraform && terraform apply

deploy:
	ansible-playbook -i hosts ansible/deploy.yml

run-local:
	cd app && uvicorn main:app --host 0.0.0.0 --port 8000

lint:
	black app/

build:
	docker build -t sentiment-api .

compose-up:
	docker-compose up --build
