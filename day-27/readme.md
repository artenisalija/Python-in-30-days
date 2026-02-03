# Day 27 - Kubernetes Local Cluster Setup

### 1. ✅ Switched to Local Kubernetes Cluster
- Switched from AWS EKS to local Rancher Desktop cluster
- Command used:
```powershell
  kubectl config use-context rancher-desktop
  kubectl get nodes
```
- Result: Connected to local single-node cluster (`desktop-pad4r0o`)

### 2. ✅ Created a Namespace
- Created dedicated namespace for organizing resources
- Commands used:
```powershell
  kubectl create namespace day-27
  kubectl get namespaces
```
- Result: Isolated workspace named `day-27`

### 3. ✅ Created a Deployment
- Created deployment.yaml file
- Deployed Docker image with 2 replicas
- Commands used:
```powershell
  code deployment.yaml
  kubectl apply -f deployment.yaml
  kubectl get deployments -n day-27
  kubectl get pods -n day-27
```
- Deployment configuration:
  - Image: `artenisal/day_26:0.0.1`
  - Replicas: 2
  - Container Port: 8000
- Result: 2 pods running your Hello World application

### 4. ✅ Created a Service (NodePort)
- Exposed application to access from browser
- Commands used:
```powershell
  code service.yaml
  kubectl apply -f service.yaml
  kubectl get services -n day-27
```
- Service configuration:
  - Type: NodePort
  - Port: 80
  - Target Port: 8000
  - Node Port: 30027
- Result: Application accessible at `http://localhost:30027`

## Files Created

### deployment.yaml
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: day-27-deployment
  namespace: day-27
spec:
  replicas: 2
  selector:
    matchLabels:
      app: day-27
  template:
    metadata:
      labels:
        app: day-27
    spec:
      containers:
      - name: hello-world
        image: artenisal/day_26:0.0.1
        ports:
        - containerPort: 8000
```

### service.yaml
```yaml
apiVersion: v1
kind: Service
metadata:
  name: day-27-service
  namespace: day-27
spec:
  type: NodePort
  selector:
    app: day-27
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8000
    nodePort: 30027
```

## Key Concepts Learned

1. **Namespaces** - Organize and isolate resources in Kubernetes
2. **Deployments** - Manage application lifecycle and replicas
3. **Pods** - The actual running containers
4. **Services** - Expose applications and provide stable networking
5. **NodePort** - Service type for accessing apps on localhost

## Useful Commands for Reference
```powershell
# View all resources in namespace
kubectl get all -n day-27

# Describe a specific pod (for debugging)
kubectl describe pod <pod-name> -n day-27

# View pod logs
kubectl logs <pod-name> -n day-27

# Watch pods in real-time
kubectl get pods -n day-27 -w

# Delete resources
kubectl delete -f deployment.yaml
kubectl delete -f service.yaml
```

## What's Next?

You've deployed a basic application! Next steps could include:
- ConfigMaps and Secrets
- Persistent Volumes
- Ingress Controllers
- Horizontal Pod Autoscaling
- Health Checks (Liveness & Readiness Probes)

---

**Date:** February 3, 2026
**Cluster:** Rancher Desktop (Local)
**Application:** Hello World (artenisal/day_26:0.0.1)