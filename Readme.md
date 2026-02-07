# 30 Days of Python & DevOps

A comprehensive 30-day learning journey covering Python development, containerization, cloud deployment, and Kubernetes orchestration.

---

## 🎯 Project Overview

This repository documents my progression from Python fundamentals to production-ready cloud-native applications. Each day builds upon the previous, covering real-world DevOps practices and modern application deployment strategies.

---

## 🛠️ Technologies Used

### Languages & Frameworks
- **Python 3.11+** - Core programming language
- **FastAPI** - Modern web framework for building APIs
- **SQLAlchemy** - SQL toolkit and ORM
- **Alembic** - Database migration tool
- **Pydantic** - Data validation using Python type hints

### Databases
- **PostgreSQL** - Relational database
- **SQLite** - Lightweight database for development

### Containerization & Orchestration
- **Docker** - Container platform
- **Docker Compose** - Multi-container orchestration
- **Kubernetes** - Container orchestration platform
- **Rancher Desktop** - Local Kubernetes environment

### Cloud Platforms & Services
- **AWS EC2** - Virtual servers
- **AWS EKS** - Elastic Kubernetes Service
- **AWS Lambda** - Serverless computing
- **AWS ECR** - Elastic Container Registry
- **AWS IAM** - Identity and Access Management

### CI/CD & Version Control
- **GitHub Actions** - Automated workflows
- **Git** - Version control
- **GitHub Container Registry (GHCR)** - Container image registry
- **DockerHub** - Public container registry

### Security & Authentication
- **JWT** - JSON Web Tokens
- **OAuth** - Authorization framework
- **Passlib** - Password hashing

### Frontend
- **HTML5/CSS3** - Structure and styling
- **Tailwind CSS** - Utility-first CSS framework
- **Vanilla JavaScript** - Client-side interactivity

### Testing & Quality
- **pytest** - Testing framework
- **Python logging** - Application logging

---

## 📂 Project Structure

```
Python-in-30-days/
┣ 📂.github/workflows/          # GitHub Actions CI/CD pipelines
┣ 📂day-1/                      # Python basics & CI automation
┣ 📂day-2/                      # Data types & conditionals
┣ 📂day-3/                      # Automation workflows
┣ 📂day-4/                      # Pure functions & side effects
┣ 📂day-5/                      # Error handling & logging
┣ 📂day-6/                      # Modular Python with Docker
┣ 📂day-7/                      # Dataclasses & JSON
┣ 📂day-8/                      # Logging & classes
┣ 📂day-9/                      # Unit testing with pytest
┣ 📂day-10/                     # Keto diet planner
┣ 📂day-11/                     # Docker image publishing to GHCR
┣ 📂day-12/                     # FastAPI + Docker optimization
┣ 📂day-13/                     # Docker Compose multi-service setup
┣ 📂day-14/                     # PostgreSQL integration
┣ 📂day-15/                     # Python scripting exercises
┣ 📂day-16/                     # AWS IAM least privilege
┣ 📂day-17/                     # FastAPI CRUD on AWS EC2
┣ 📂day-18/                     # FastAPI health check endpoint
┣ 📂day-19/                     # RESTful API with FastAPI
┣ 📂day-20/                     # CRUD with SQLAlchemy
┣ 📂day-21/                     # JWT & OAuth authentication
┣ 📂day-22/                     # EC2 deployment from GHCR
┣ 📂day-23/                     # Structured FastAPI app
┣ 📂day-24/                     # AWS Lambda function deployment
┣ 📂day-25/                     # Kubernetes introduction
┣ 📂day-26/                     # EKS cluster deployment
┣ 📂day-27/                     # Kubernetes namespaces & services
┣ 📂day-28/                     # ConfigMaps, Secrets, Persistent Volumes
┣ 📂day-29/                     # CI/CD pipeline to Kubernetes
┗ 📂day-30/                     # 12 Factor Blog Application
```

---

## 🗺️ Day-by-Day Navigation

### Week 1: Python Fundamentals & CI/CD
| Day | Focus | Key Concepts | Location |
|-----|-------|--------------|----------|
| **Day 1** | Python Basics & CI | Environment variables, GitHub Actions | [`/day-1`](./day-1) |
| **Day 2** | Data Types | Lists, dictionaries, mutability | [`/day-2`](./day-2) |
| **Day 3** | Automation | Automated testing workflows | [`/day-3`](./day-3) |
| **Day 4** | Pure Functions | Function design, side effects | [`/day-4`](./day-4) |
| **Day 5** | Error Handling | Custom errors, logging, validation | [`/day-5`](./day-5) |
| **Day 6** | Modular Python | Project structure, Docker | [`/day-6`](./day-6) |
| **Day 7** | Dataclasses & JSON | Object serialization | [`/day-7`](./day-7) |

### Week 2: Testing, Logging & Containerization
| Day | Focus | Key Concepts | Location |
|-----|-------|--------------|----------|
| **Day 8** | Logging & Classes | OOP, structured logging | [`/day-8`](./day-8) |
| **Day 9** | Unit Testing | pytest, Docker testing | [`/day-9`](./day-9) |
| **Day 10** | Containerization | Dockerfile, diet planner app | [`/day-10`](./day-10) |
| **Day 11** | Container Registry | GHCR, image publishing | [`/day-11`](./day-11) |
| **Day 12** | FastAPI Optimization | Layer caching, slim images | [`/day-12`](./day-12) |
| **Day 13** | Docker Compose | Multi-service architecture | [`/day-13`](./day-13) |
| **Day 14** | Database Integration | PostgreSQL, psycopg2 | [`/day-14`](./day-14) |

### Week 3: Cloud Deployment & APIs
| Day | Focus | Key Concepts | Location |
|-----|-------|--------------|----------|
| **Day 15** | Python Scripting | Advanced scripting | [`/day-15`](./day-15) |
| **Day 16** | AWS IAM | Least privilege principle | [`/day-16`](./day-16) |
| **Day 17** | EC2 Deployment | VPC, Docker on EC2 | [`/day-17`](./day-17) |
| **Day 18** | Health Checks | API monitoring | [`/day-18`](./day-18) |
| **Day 19** | RESTful API | CRUD operations, routing | [`/day-19`](./day-19) |
| **Day 20** | SQLAlchemy ORM | Database models, migrations | [`/day-20`](./day-20) |
| **Day 21** | Authentication | JWT, OAuth, password hashing | [`/day-21`](./day-21) |

### Week 4: Advanced Cloud & Kubernetes
| Day | Focus | Key Concepts | Location |
|-----|-------|--------------|----------|
| **Day 22** | EC2 from GHCR | Container deployment | [`/day-22`](./day-22) |
| **Day 23** | App Structure | Modular FastAPI design | [`/day-23`](./day-23) |
| **Day 24** | AWS Lambda | Serverless, ECR, Mangum | [`/day-24`](./day-24) |
| **Day 25** | Kubernetes Intro | Pods, deployments, services | [`/day-25`](./day-25) |
| **Day 26** | EKS Deployment | AWS EKS, eksctl, LoadBalancer | [`/day-26`](./day-26) |
| **Day 27** | K8s Resources | Namespaces, NodePort | [`/day-27`](./day-27) |
| **Day 28** | K8s Advanced | ConfigMaps, Secrets, PVs | [`/day-28`](./day-28) |

### Week 5: Production-Ready Applications
| Day | Focus | Key Concepts | Location |
|-----|-------|--------------|----------|
| **Day 29** | CI/CD to K8s | Automated deployments, rolling updates | [`/day-29`](./day-29) |
| **Day 30** | 12 Factor App | Full-stack blog with best practices | [`/day-30`](./day-30) |

---

## 🚀 Quick Start

### Prerequisites
```bash
# Required tools
- Python 3.11+
- Docker & Docker Compose
- kubectl (for Kubernetes projects)
- AWS CLI (for AWS projects)
```

### Running a Project
```bash
# Navigate to any day folder
cd day-XX

# Check the day's README for specific instructions
cat README.md

# Most Docker projects can be run with:
docker build -t day-xx .
docker run -p 8000:8000 day-xx
```

---

## 🎓 Key Learnings

### Development Practices
✅ Test-driven development with pytest  
✅ Modular code organization  
✅ Environment-based configuration  
✅ Logging and error handling  
✅ API documentation with FastAPI  

### DevOps & Deployment
✅ Docker containerization & optimization  
✅ Multi-stage Docker builds  
✅ Docker Compose orchestration  
✅ CI/CD with GitHub Actions  
✅ Container registry management  

### Cloud & Infrastructure
✅ AWS EC2 instance management  
✅ AWS Lambda serverless functions  
✅ AWS IAM security policies  
✅ Kubernetes cluster deployment  
✅ EKS production setup  

### Kubernetes Expertise
✅ Deployments, Services, Pods  
✅ ConfigMaps & Secrets  
✅ Persistent Volumes  
✅ Namespaces & resource isolation  
✅ Rolling updates & zero-downtime deploys  

### Application Architecture
✅ RESTful API design  
✅ JWT authentication  
✅ Database migrations with Alembic  
✅ 12 Factor App methodology  
✅ Full-stack development  

---

## 📊 Project Highlights

### Most Complex Projects

**Day 30 - 12 Factor Blog Application**
- Complete full-stack application
- FastAPI backend with PostgreSQL
- JWT authentication & authorization
- Alembic database migrations
- HTML/CSS/JS frontend with Tailwind
- Docker Compose multi-service setup
- Production-ready architecture

**Day 29 - CI/CD Pipeline to Kubernetes**
- Automated Docker builds
- DockerHub integration
- Kubernetes deployments
- Rolling updates
- Zero-downtime deployments

**Day 26 - EKS Cluster Deployment**
- AWS EKS setup with eksctl
- LoadBalancer service configuration
- Production Kubernetes cluster

**Day 21 - JWT & OAuth Authentication**
- Secure user authentication
- Password hashing with Passlib
- Token-based authorization
- Protected API endpoints

---

## 🔗 Useful Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Docker Documentation](https://docs.docker.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [AWS Documentation](https://docs.aws.amazon.com/)
- [12 Factor App](https://12factor.net/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

---

## 📝 Notes

- Each day builds incrementally on previous concepts
- All projects include README files with specific instructions
- GitHub Actions workflows automate testing where applicable
- Docker is used extensively for consistent environments
- Focus shifts from fundamentals → APIs → cloud → Kubernetes

---

## 🏆 Completion Status

**Days Completed:** 30/30 ✅

**Skills Acquired:**
- Python development
- API design & implementation
- Docker & containerization
- Kubernetes orchestration
- AWS cloud services
- CI/CD automation
- Database management
- Authentication & security
- Full-stack development

---

**Author:** Artenis Alija  
**Duration:** 30 Days  
**Start Date:** 8th January 2026 
**End Date:** 7th February 2026