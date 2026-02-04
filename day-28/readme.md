# Day 29 - Kubernetes ConfigMaps, Secrets & Persistent Volumes

## What I Learned Today 🎓

Today I took my Kubernetes knowledge to the next level by learning how to manage configuration, handle sensitive data, and persist storage across pod restarts. I built on my Day 27 foundation and added three critical components that are essential for real-world applications.

---

## Key Concepts I Mastered

### 1. ConfigMaps - External Configuration Management

**What I learned:**
ConfigMaps allow me to separate configuration from my application code. This means I can change settings without rebuilding my Docker image!

**The Big Realization:**
- **Without ConfigMaps:** Change config → Rebuild image → Push to Docker Hub → Redeploy (10+ minutes)
- **With ConfigMaps:** Change ConfigMap → Apply → Restart pods (30 seconds)

**Key Insight:** ConfigMaps store NON-SENSITIVE data like:
- Database URLs
- API endpoints
- Feature flags
- Log levels
- Environment-specific settings

**Important Note:** ConfigMaps are NOT the actual services! They only store the configuration/addresses. I still need to run actual database containers, API containers, etc. ConfigMaps just tell my app WHERE to find them.

---

### 2. Secrets - Secure Sensitive Data Storage

**What I learned:**
Secrets work almost exactly like ConfigMaps, but they're specifically designed for sensitive information.

**Key Differences from ConfigMaps:**
- Data is base64-encoded (obfuscated, not fully encrypted by default)
- Kubernetes handles them more carefully (doesn't log them, restricts access)
- Used for passwords, API keys, tokens, certificates

**What I stored in Secrets:**
- Database passwords
- API keys
- JWT tokens

**Important Security Note:** While Secrets are "hidden" in `kubectl describe`, they're not truly encrypted by default. In production, I'd use additional security like encryption at rest or external secret managers (AWS Secrets Manager, HashiCorp Vault).

---

### 3. Persistent Volumes - Data That Survives

**What I learned:**
Containers are ephemeral (temporary). When a pod crashes or restarts, all data inside is GONE. Persistent Volumes solve this problem!

**The Three Components:**

1. **PersistentVolume (PV)** - The actual storage (like a hard drive)
2. **PersistentVolumeClaim (PVC)** - A "request" for storage (like reserving space)
3. **Mount in Pod** - Connect the storage to the container

**Real-World Use Cases:**
- Database files
- User uploaded images/files
- Application logs
- Any data that must survive pod restarts

**What I Proved:** I created a file in one pod, deleted that pod, and the file appeared in the brand new pod! The data survived because it was stored in the Persistent Volume, not inside the container.

---

## Step-by-Step What I Did

### Initial Setup

**1. Verified my local cluster connection:**
```powershell
kubectl config get-contexts
# Confirmed I was on rancher-desktop
```

**2. Created a new namespace for Day 29:**
```powershell
kubectl create namespace day-29
kubectl get namespaces
```

---

### Building the Base Application

**3. Created the deployment:**
```powershell
cd day-29
code deployment.yaml
kubectl apply -f deployment.yaml
kubectl get pods -n day-29
# Waited for 2 pods to be Running
```

**4. Created the service:**
```powershell
code service.yaml
kubectl apply -f service.yaml
kubectl get services -n day-29
# Verified app accessible at http://localhost:30029
```

---

### Adding ConfigMaps

**5. Created a ConfigMap:**
```powershell
code configmap.yaml
kubectl apply -f configmap.yaml
kubectl get configmap -n day-29
kubectl describe configmap day-29-config -n day-29
```

**6. Updated deployment to use ConfigMap:**
```powershell
code deployment.yaml
# Modified env section to use configMapKeyRef instead of hardcoded values
kubectl apply -f deployment.yaml
kubectl rollout restart deployment/day-29-deployment -n day-29
```

**7. Verified ConfigMap values inside the pod:**
```powershell
kubectl get pods -n day-29
kubectl exec -it <pod-name> -n day-29 -- env
# Saw APP_NAME, ENVIRONMENT, LOG_LEVEL, GREETING_MESSAGE from ConfigMap
```

**8. TESTED LIVE UPDATE - Changed ConfigMap without rebuilding image:**
```powershell
code configmap.yaml
# Changed GREETING_MESSAGE value
kubectl apply -f configmap.yaml
kubectl rollout restart deployment/day-29-deployment -n day-29
kubectl exec -it <new-pod-name> -n day-29 -- env | Select-String "GREETING_MESSAGE"
# Saw the NEW value! No Docker rebuild needed!
```

---

### Adding Secrets

**9. Created a Secret:**
```powershell
code secret.yaml
kubectl apply -f secret.yaml
kubectl get secrets -n day-29
kubectl describe secret day-29-secret -n day-29
# Notice: Values are HIDDEN for security!
```

**10. Updated deployment to use Secrets:**
```powershell
code deployment.yaml
# Added secretKeyRef for DB_PASSWORD, API_KEY, JWT_SECRET
kubectl apply -f deployment.yaml
kubectl rollout restart deployment/day-29-deployment -n day-29
```

**11. Verified Secrets inside the pod:**
```powershell
kubectl get pods -n day-29
kubectl exec -it <pod-name> -n day-29 -- env | Select-String "DB_PASSWORD"
# Saw the secret value injected as environment variable
```

---

### Adding Persistent Volumes

**12. Created a PersistentVolume:**
```powershell
code persistentvolume.yaml
kubectl apply -f persistentvolume.yaml
kubectl get pv
# Saw status: Available
```

**13. Created a PersistentVolumeClaim:**
```powershell
code persistentvolumeclaim.yaml
kubectl apply -f persistentvolumeclaim.yaml
kubectl get pvc -n day-29
# Saw status: Bound (successfully claimed the PV)
kubectl get pv
# PV status changed to: Bound
```

**14. Updated deployment to mount the PVC:**
```powershell
code deployment.yaml
# Added volumes section at spec level
# Added volumeMounts inside container
kubectl apply -f deployment.yaml
kubectl rollout restart deployment/day-29-deployment -n day-29
```

**15. TESTED PERSISTENT STORAGE - Proved data survives pod deletion:**
```powershell
kubectl get pods -n day-29
# Got pod name: day-29-deployment-5d6cc9586c-d47n9

# Created a test file
kubectl exec -it day-29-deployment-5d6cc9586c-d47n9 -n day-29 -- sh -c "echo 'Hello from Persistent Storage!' > /app/data/test.txt"

# Verified file exists
kubectl exec -it day-29-deployment-5d6cc9586c-d47n9 -n day-29 -- cat /app/data/test.txt
# Output: Hello from Persistent Storage!

# DELETED the pod
kubectl delete pod day-29-deployment-5d6cc9586c-d47n9 -n day-29

# Watched new pod appear
kubectl get pods -n day-29 -w

# Got new pod name and checked if file still exists
kubectl exec -it <new-pod-name> -n day-29 -- cat /app/data/test.txt
# SUCCESS! File was still there in the NEW pod!
```

---

## Files I Created

### deployment.yaml
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: day-29-deployment
  namespace: day-29
spec:
  replicas: 2
  selector:
    matchLabels:
      app: day-29
  template:
    metadata:
      labels:
        app: day-29
    spec:
      containers:
      - name: hello-world
        image: artenisal/day_26:0.0.1
        ports:
        - containerPort: 8000
        volumeMounts:
        - name: data-storage
          mountPath: /app/data
        env:
        - name: APP_NAME
          valueFrom:
            configMapKeyRef:
              name: day-29-config
              key: APP_NAME
        - name: ENVIRONMENT
          valueFrom:
            configMapKeyRef:
              name: day-29-config
              key: ENVIRONMENT
        - name: LOG_LEVEL
          valueFrom:
            configMapKeyRef:
              name: day-29-config
              key: LOG_LEVEL
        - name: GREETING_MESSAGE
          valueFrom:
            configMapKeyRef:
              name: day-29-config
              key: GREETING_MESSAGE
        - name: DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: day-29-secret
              key: DB_PASSWORD
        - name: API_KEY
          valueFrom:
            secretKeyRef:
              name: day-29-secret
              key: API_KEY
        - name: JWT_SECRET
          valueFrom:
            secretKeyRef:
              name: day-29-secret
              key: JWT_SECRET
      volumes:
      - name: data-storage
        persistentVolumeClaim:
          claimName: day-29-pvc
```

### service.yaml
```yaml
apiVersion: v1
kind: Service
metadata:
  name: day-29-service
  namespace: day-29
spec:
  type: NodePort
  selector:
    app: day-29
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8000
    nodePort: 30029
```

### configmap.yaml
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: day-29-config
  namespace: day-29
data:
  APP_NAME: "Day 29 - Hello World with ConfigMap"
  ENVIRONMENT: "local-kubernetes"
  LOG_LEVEL: "DEBUG"
  GREETING_MESSAGE: "ConfigMap UPDATED! I changed this without rebuilding the Docker image!"
  
  app.properties: |
    app.version=2.0.0
    app.author=artenisal
    feature.configmap=enabled
    feature.secrets=coming-next
```

### secret.yaml
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: day-29-secret
  namespace: day-29
type: Opaque
stringData:
  DB_PASSWORD: "superSecretPassword123"
  API_KEY: "sk_live_abc123xyz789"
  JWT_SECRET: "my-super-secret-jwt-token"
```

### persistentvolume.yaml
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: day-29-pv
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: /mnt/data/day-29
  storageClassName: manual
```

### persistentvolumeclaim.yaml
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: day-29-pvc
  namespace: day-29
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
  storageClassName: manual
```

---

## Key Takeaways & "Aha!" Moments

### 1. Configuration vs Code
I now understand that **changing configuration doesn't require rebuilding images!** This is a game-changer for:
- Switching between dev/staging/prod environments
- A/B testing feature flags
- Updating API endpoints
- Changing database connections

### 2. ConfigMaps Are NOT Services
Important realization: ConfigMaps store the **address/configuration** of services, NOT the services themselves. I still need to run actual database pods, API pods, etc. ConfigMaps just tell my app WHERE to connect.

### 3. Secrets Aren't Fully Encrypted by Default
While Secrets are base64-encoded and handled more carefully than ConfigMaps, they're not encrypted by default in Kubernetes. For production, I'd need additional security measures.

### 4. Persistent Storage Is Critical
Without PersistentVolumes, any data my app writes is lost when pods restart. For databases, user uploads, or any stateful application, PersistentVolumes are ESSENTIAL.

### 5. Pods Don't Auto-Reload ConfigMap Changes
When I change a ConfigMap, running pods don't automatically know. I must restart them with `kubectl rollout restart` to pick up new values. (There are advanced patterns for auto-reloading, but that's beyond basics.)

---

## Useful Commands I Used

```powershell
# View all resources in namespace
kubectl get all -n day-29

# Describe resources for detailed info
kubectl describe configmap day-29-config -n day-29
kubectl describe secret day-29-secret -n day-29
kubectl describe pod <pod-name> -n day-29

# Execute commands inside pods
kubectl exec -it <pod-name> -n day-29 -- env
kubectl exec -it <pod-name> -n day-29 -- cat /app/data/test.txt
kubectl exec -it <pod-name> -n day-29 -- sh

# Restart deployment to pick up changes
kubectl rollout restart deployment/day-29-deployment -n day-29

# Watch pods in real-time
kubectl get pods -n day-29 -w

# Delete pods (they auto-recreate)
kubectl delete pod <pod-name> -n day-29

# Check PersistentVolumes and Claims
kubectl get pv
kubectl get pvc -n day-29
```

---

## Architecture Overview

My Day 29 cluster now has:

```
┌─────────────────────────────────────────────────────────┐
│                   Rancher Desktop Cluster                │
│                                                           │
│  ┌─────────────────────────────────────────────────┐   │
│  │              Namespace: day-29                   │   │
│  │                                                   │   │
│  │  ┌──────────────────────────────────────────┐  │   │
│  │  │  Deployment: day-29-deployment           │  │   │
│  │  │  - Replicas: 2                           │  │   │
│  │  │  - Image: artenisal/day_26:0.0.1         │  │   │
│  │  │  - Reads: ConfigMap + Secrets            │  │   │
│  │  │  - Mounts: PersistentVolumeClaim         │  │   │
│  │  └──────────────────────────────────────────┘  │   │
│  │                                                   │   │
│  │  ┌──────────────────────────────────────────┐  │   │
│  │  │  Service: day-29-service                 │  │   │
│  │  │  - Type: NodePort                        │  │   │
│  │  │  - Port: 30029                           │  │   │
│  │  │  - Access: http://localhost:30029        │  │   │
│  │  └──────────────────────────────────────────┘  │   │
│  │                                                   │   │
│  │  ┌──────────────────────────────────────────┐  │   │
│  │  │  ConfigMap: day-29-config                │  │   │
│  │  │  - APP_NAME, ENVIRONMENT, LOG_LEVEL      │  │   │
│  │  │  - GREETING_MESSAGE, app.properties      │  │   │
│  │  └──────────────────────────────────────────┘  │   │
│  │                                                   │   │
│  │  ┌──────────────────────────────────────────┐  │   │
│  │  │  Secret: day-29-secret                   │  │   │
│  │  │  - DB_PASSWORD, API_KEY, JWT_SECRET      │  │   │
│  │  └──────────────────────────────────────────┘  │   │
│  │                                                   │   │
│  │  ┌──────────────────────────────────────────┐  │   │
│  │  │  PersistentVolumeClaim: day-29-pvc       │  │   │
│  │  │  - Storage: 1Gi                          │  │   │
│  │  │  - Bound to: day-29-pv                   │  │   │
│  │  └──────────────────────────────────────────┘  │   │
│  └─────────────────────────────────────────────────┘   │
│                                                           │
│  ┌─────────────────────────────────────────────────┐   │
│  │  PersistentVolume: day-29-pv (Cluster-level)    │   │
│  │  - Capacity: 1Gi                                 │   │
│  │  - HostPath: /mnt/data/day-29                    │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

---

## What's Next?

Now that I understand ConfigMaps, Secrets, and Persistent Volumes, I'm ready to explore:

- **Ingress Controllers** - HTTP routing and load balancing
- **Horizontal Pod Autoscaler** - Auto-scaling based on CPU/memory
- **Health Checks** - Liveness and Readiness probes
- **StatefulSets** - For stateful applications like databases
- **DaemonSets** - Running pods on every node
- **Jobs and CronJobs** - Scheduled and one-time tasks

---

**Date:** February 4, 2026  
**Cluster:** Rancher Desktop (Local)  
**Application:** Hello World (artenisal/day_26:0.0.1)  
**New Skills:** ConfigMaps, Secrets, Persistent Volumes

---

## The Most Important Thing I Learned Today

**Kubernetes separates concerns beautifully:**
- **Code** lives in Docker images
- **Configuration** lives in ConfigMaps
- **Sensitive data** lives in Secrets
- **Persistent data** lives in PersistentVolumes

This separation makes applications more flexible, secure, and maintainable! 🚀
