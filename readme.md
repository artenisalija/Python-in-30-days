## Day-22 Deploy Day-21 App into EC2

1. Logged in in docker 
2. Tagged the image day_21
3. Pushed the image into GHCR
4. Logged into a newly created EC2 using SSH
5. Updated Ubuntu and install Docker
6. Allow your user to run Docker without 'sudo'
7. Log in from GHCR to EC2
8. Pulled Docker image
9. Run container
10. Verified it’s running

```cmd 
1. docker login --username USER --password GHCR_TOKEN ghcr.io 
2. docker tag day_21 ghcr.io/<GITHUB_USERNAME>/day_21:latest
3. docker push ghcr.io/<GITHUB_USERNAME>/day_21:latest
4. ssh -i "KEY" ubuntu@13.60.15.16
5. sudo apt update
- sudo apt install -y apt-transport-https ca-certificates curl software-properties-common gnupg lsb-release
- curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
- echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/   linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
- sudo apt update
- sudo apt install -y docker-ce docker-ce-cli containerd.io
6. sudo usermod -aG docker ubuntu
7. echo <YOUR_GITHUB_TOKEN> | docker login ghcr.io -u <GITHUB_USERNAME> --password-stdin
8. docker pull ghcr.io/<GITHUB_USERNAME>/day_21:latest
9. docker run -d --name day_21_container -p 8000:8000 ghcr.io/<GITHUB_USERNAME>/day_21:latest
10. docker ps




