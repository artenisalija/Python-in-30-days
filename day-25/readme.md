## Day 25 - Installing and Understanding the need for Kubernetes

1. Intalled Rancher Desktop by Suse
2. Created Simple Hello World App using Fatsapi
3. Created Image and container
4. Pushed image container to Docker Hub
5. Checked Status of cluster from Rancher
6. Deployed Docker image into the cluster
7. Exposed the pod as a service
8. Opened the app in my browser (http://localhost:NodePort)


```cmd
Docker Hub
- docker build -t day_25 .
- docker run -d -p 8000:8000 day_25  
- docker build -t artenisal/day_25:0.0.1 .
- docker push artenisal/day_25:0.0.1   

Kubernetes
- config current-context
- config get-contexts
- kubectl config use-context rancher-desktop
- kubectl get nodes

Deployment of Docker image into cluster
- kubectl create deployment my-app --image=<dockerhub-username>/<image-name>:<tag>
- kubectl expose deployment my-app --type=NodePort --port=8000
- kubectl get services


