## Day 26 - Cluster Deployment into EKS

1. Created Cluster in EKS using powershell
2. Created two files ```deployment.yaml``` and ```service.yaml ```
3. Deployed to EKS using kubectl
4. Checked the deployment and service status using kubectl commands
5. Accessed the application using the LoadBalancer URL

```cmd
eksctl create cluster `
  --name day-26-cluster `
  --region us-east-1 `
  --nodegroup-name standard-workers `
  --node-type t3.medium `
  --nodes 2
```

```
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```