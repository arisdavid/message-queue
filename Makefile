dev-configure:
	pip install -r requirements-dev.txt
	pre-commit install

build:
	# Eval to build images inside minikube cluster
	eval $(minikube docker-env)
	docker build -t producer:latest -f producer/Dockerfile .
	docker build -t consumer:latest -f consumer/Dockerfile .

install-rabbitmq:
	helm repo add bitnami https://charts.bitnami.com/bitnami
	helm install minikube-rabbitmq bitnami/rabbitmq --namespace=practice --set auth.username=admin,auth.password=admin

uninstall-rabbitmq:
	helm uninstall minikube-rabbitmq --namespace=practice

install-minikube:
	kubectl apply -f minikube-deployment.yaml --namespace=practice

uninstall-minikube:
	kubectl delete -f minikube-deployment.yaml --namespace=practice

rmq-creds:
	kubectl --namespace practice create secret generic rmq-creds --from-env-file=.env.secret