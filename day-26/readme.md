## Day 26 - Cluster Deployment into EKS

1. Created Cluster in EKS using powershell
2. Created two files ```deployment.yaml``` and ```service.yaml ```
3. 

```cmd
eksctl create cluster `
  --name day-26-cluster `
  --region eu-north-1 `
  --nodegroup-name standard-workers `
  --node-type t3.medium `
  --nodes 2
```

```

```