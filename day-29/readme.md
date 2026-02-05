# Day 29 - CI/CD Pipeline to Kubernetes

A complete CI/CD pipeline using GitHub Actions to automatically build, push, and deploy a FastAPI application to Kubernetes.

## 🚀 Overview

This project demonstrates a full CI/CD workflow that:
- Automatically builds Docker images on every commit
- Pushes images to DockerHub with unique SHA tags
- Deploys to a local Kubernetes cluster (Rancher Desktop)
- Implements rolling updates for zero-downtime deployments

## 📁 Project Structure
```
day-29/
├── app/
│   └── main.py              # FastAPI application
├── k8s/
│   ├── deployment.yaml      # Kubernetes deployment manifest
│   └── service.yaml         # Kubernetes service manifest
├── Dockerfile               # Docker image configuration
└── requirements.txt         # Python dependencies
```

## 🛠️ Technologies Used

- **FastAPI** - Modern Python web framework
- **Docker** - Container platform
- **Kubernetes** - Container orchestration
- **GitHub Actions** - CI/CD automation
- **DockerHub** - Container registry
- **Rancher Desktop** - Local Kubernetes environment

## 📋 Prerequisites

- Docker installed
- Kubernetes cluster (Rancher Desktop, Minikube, or EKS)
- kubectl configured
- DockerHub account

## 🔧 Setup Instructions

### Create Kubernetes Namespace
```bash
kubectl create namespace day-29
```

### Deploy to Kubernetes
```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### Verify Deployment
```bash
kubectl get pods -n day-29
kubectl get svc -n day-29
```

### Access the Application
```bash
# Get the NodePort
kubectl get svc day29-service -n day-29

# Access via curl
curl http://localhost:<NODE_PORT>
```

## 🔄 CI/CD Workflow

### Pipeline Flow

1. Push code to GitHub
2. GitHub Actions builds Docker image
3. Image tagged with commit SHA and `latest`
4. Image pushed to DockerHub
5. Restart Kubernetes deployment to pull new image

### Making Updates
```bash
# 1. Make code changes locally
# 2. Commit and push to trigger pipeline
# 3. Wait for build to complete
# 4. Restart deployment

kubectl rollout restart deployment day29-app -n day-29
kubectl rollout status deployment day29-app -n day-29
```

## 📦 Docker Image

**Repository**: `artenisal/day-29`

**Tags**:
- `latest` - Most recent build
- `main-<sha>` - Specific commit builds
```bash
# Pull image
docker pull artenisal/day-29:latest

# Run locally
docker run -p 8000:8000 artenisal/day-29:latest
```

## 🎯 API Endpoints

- `GET /` - Hello World message
- `GET /health` - Health check endpoint
- `GET /docs` - FastAPI automatic documentation

## 🔍 Useful Commands

### Kubernetes
```bash
# View pods
kubectl get pods -n day-29

# View logs
kubectl logs -f -l app=day29-app -n day-29

# Describe deployment
kubectl describe deployment day29-app -n day-29

# Restart deployment
kubectl rollout restart deployment day29-app -n day-29

# Check rollout status
kubectl rollout status deployment day29-app -n day-29

# Delete resources
kubectl delete -f k8s/deployment.yaml
kubectl delete -f k8s/service.yaml

# Delete namespace
kubectl delete namespace day-29
```

### Docker
```bash
# Build image locally
docker build -t artenisal/day-29:latest .

# Run container
docker run -p 8000:8000 artenisal/day-29:latest

# View logs
docker logs <container-id>

# Remove image
docker rmi artenisal/day-29:latest
```

## 🎓 Key Learnings

- Automated Docker image builds with GitHub Actions
- Container registry integration (DockerHub)
- Kubernetes deployment strategies
- Rolling updates and zero-downtime deployments
- Image tagging strategies (latest vs SHA)
- Kubernetes namespace management
- Service exposure via NodePort
- Container resource management

## 🚀 Production Deployment (AWS EKS)

For production deployments to AWS EKS, the GitHub Actions workflow can automatically deploy by configuring AWS credentials and kubectl access in the pipeline.

---

**Day 29** of the 30 Days Python Challenge