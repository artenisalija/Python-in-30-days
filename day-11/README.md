Day 11 – Docker Image on GitHub Container Registry

Created a simple Docker image and published it to the GitHub Container Registry (GHCR). I wrote a basic Dockerfile, built a container that runs a simple Python script, and generated a GitHub Personal Access Token (PAT) with read, write, and delete package permissions (7-day expiration). I authenticated with GHCR using Docker, pushed the image to the registry, and verified that it appears under GitHub → Packages, where GitHub also provides a command to pull the image in the future.

```bash
docker login --username MY_USERNAME --password MY_TOKEN ghcr.io
docker push ghcr.io/artenisalija/hello-world-ghcr:latest
