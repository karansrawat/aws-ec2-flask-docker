# Flask App on AWS EC2 with Docker

A small Flask web app packaged in a Docker container and run on an AWS EC2 Linux server. A GitHub Actions workflow builds the image and checks the app on every push.

## What I used
- Python, Flask, Gunicorn
- Docker
- AWS EC2 (Ubuntu)
- Linux commands and SSH
- GitHub Actions (build and health check)

## Project files

```
.
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── setup-ec2.sh                       # installs Docker on EC2
├── .gitignore
├── .github/workflows/docker-build.yml # CI check
└── README.md
```

## Step 1: Try it on your own computer

```bash
docker build -t flask-app .
docker run -p 5000:5000 flask-app
```

Open http://localhost:5000

## Step 2: Launch an EC2 instance

1. AWS Console -> **EC2** -> **Launch instance**.
2. Name: `flask-docker-server`.
3. AMI: **Ubuntu Server 24.04 LTS**.
4. Instance type: **t2.micro** or **t3.micro** (free tier).
5. Key pair: **Create new key pair**, download the `.pem` file and keep it safe.
6. Network settings -> **Edit** -> Security group rules:
   - SSH (port 22): source **My IP**
   - Custom TCP, port **5000**: source **Anywhere (0.0.0.0/0)**
7. Click **Launch instance** and copy the **Public IPv4 address**.

## Step 3: Connect to the server

On Linux/Mac:

```bash
chmod 400 your-key.pem
ssh -i your-key.pem ubuntu@<PUBLIC_IP>
```

On Windows, use PowerShell or Git Bash with the same command.

## Step 4: Install Docker and get the code

```bash
sudo apt update
sudo apt install -y git
git clone https://github.com/<your-username>/aws-ec2-flask-docker.git
cd aws-ec2-flask-docker
bash setup-ec2.sh
```

Log out (`exit`) and SSH back in so Docker permissions apply.

## Step 5: Build and run the container

```bash
cd aws-ec2-flask-docker
docker build -t flask-app .
docker run -d --name flask-app --restart unless-stopped -p 5000:5000 flask-app
docker ps
```

## Step 6: Open it in your browser

```
http://<PUBLIC_IP>:5000
http://<PUBLIC_IP>:5000/health
```

## Updating the app later

```bash
cd aws-ec2-flask-docker
git pull
docker build -t flask-app .
docker stop flask-app && docker rm flask-app
docker run -d --name flask-app --restart unless-stopped -p 5000:5000 flask-app
```

## Useful commands I practiced

| Command | What it does |
|---------|--------------|
| `docker ps` | List running containers |
| `docker logs flask-app` | See app logs |
| `docker stop flask-app` | Stop the container |
| `df -h` | Check disk space |
| `top` | See CPU and memory use |

## Clean up (avoid charges)
Terminate the EC2 instance from the console when you are finished.

## What I learned
- Launching and connecting to a Linux server on AWS
- Security groups and SSH key pairs
- Writing a Dockerfile and running containers
- Basic Linux commands
- Running an automated build check with GitHub Actions

## Screenshots
Add screenshots of the app in the browser, the EC2 instance running, and the green GitHub Actions check.
