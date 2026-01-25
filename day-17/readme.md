Day 17 - FastAPI CRUD App Deployment on AWS EC2 with Docker

Created a simple CRUD FastAPI application that runs locally.  
Built a Docker image for the application and pushed it to GitHub Container Registry (GHCR).  
Created an AWS EC2 instance using an AWS AMI and configured a VPC.  
Pulled the Docker image on the EC2 instance and ran it as a container.

## EC2 Setup and Docker Installation

Connected to the EC2 instance:
- `ssh -i "day-17-key-pair.pem" ec2-user@PUBLIC_IP`

Updated the system and installed Docker:
- `sudo dnf update -y`
- `sudo dnf install docker -y`

Started and enabled Docker:
- `sudo systemctl start docker`
- `sudo systemctl enable docker`
- `sudo systemctl status docker`

Allowed the EC2 user to run Docker without sudo:
- `sudo usermod -aG docker ec2-user`

Exited SSH to apply group changes:
- `exit`

## Docker Verification

Verified Docker installation:
- `docker --version`
- `docker run hello-world`

## Application Deployment from GHCR

Logged in to GitHub Container Registry using a Personal Access Token:
- `echo "<YOUR_PERSONAL_ACCESS_TOKEN>" | docker login ghcr.io -u artenisalija --password-stdin`

Pulled the Docker image:
- `docker pull ghcr.io/artenisalija/hello-world-ghcr:latest`

Verified the image exists locally:
- `docker images`

## Running and Verifying the Container

Ran the container:
- `docker run -it ghcr.io/artenisalija/hello-world-ghcr:latest /bin/sh`

Checked container status:
- `docker ps -a`

Checked container logs:
- `docker logs CONTAINER_NAME`

Expected result: container logs display **"Hello World"**, confirming successful execution.
