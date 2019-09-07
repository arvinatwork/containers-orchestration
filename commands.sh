#! bin/bash

#Single docker
docker pull wordpress
docker run --name demo-wordpress1 -p 8050:80 -d wordpress

#app
docker run -d -p 5000:5000 demo_app:latest

# Kubernetes
kubectl create deployment hello-node --image=gcr.io/hello-minikube-zero-install/hello-node
kubectl run hello-minikube --image=k8s.gcr.io/echoserver:1.10 --port=8070
kubectl get deployments
kubectl get pods