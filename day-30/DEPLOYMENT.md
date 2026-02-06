# Deployment Guide - Docker Hub & Production 🚀

## Part 1: Build and Push to Docker Hub

### Step 1: Build Your Image

```bash
# Replace 'artenisal' with your Docker Hub username
docker build -t artenisal/blog-api:1.0.0 .

# Also tag as 'latest'
docker tag artenisal/blog-api:1.0.0 artenisal/blog-api:latest
```

### Step 2: Login to Docker Hub

```bash
docker login
# Enter your Docker Hub username and password
```

### Step 3: Push to Docker Hub

```bash
# Push specific version
docker push artenisal/blog-api:1.0.0

# Push latest
docker push artenisal/blog-api:latest
```

### Step 4: Verify on Docker Hub

Go to https://hub.docker.com/r/artenisal/blog-api and verify your image is there!

---

## Part 2: Deploy Anywhere

### Option A: Docker Compose (Recommended for Small Projects)

**Create `docker-compose.prod.yml` on your server:**

```yaml
version: '3.8'

services:
  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: bloguser
      POSTGRES_PASSWORD: CHANGE-THIS-PASSWORD
      POSTGRES_DB: blogdb
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: always

  api:
    image: artenisal/blog-api:latest  # Your Docker Hub image
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql://bloguser:CHANGE-THIS-PASSWORD@postgres:5432/blogdb
      SECRET_KEY: CHANGE-THIS-TO-RANDOM-SECRET
      ALGORITHM: HS256
      ACCESS_TOKEN_EXPIRE_MINUTES: 30
      ENVIRONMENT: production
      CORS_ORIGINS: https://yourdomain.com
    depends_on:
      - postgres
    restart: always

  frontend:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./frontend:/usr/share/nginx/html
    restart: always

volumes:
  postgres_data:
```

**Deploy:**

```bash
# On your server
docker-compose -f docker-compose.prod.yml up -d
```

---

### Option B: Single Container (API Only)

```bash
# Run just the API (you'll need external PostgreSQL)
docker run -d \
  --name blog-api \
  -p 8000:8000 \
  -e DATABASE_URL="postgresql://user:pass@host:5432/db" \
  -e SECRET_KEY="your-super-secret-key-change-this" \
  -e ENVIRONMENT="production" \
  --restart always \
  artenisal/blog-api:latest
```

---

### Option C: Deploy to AWS ECS

**1. Create Task Definition (use AWS Console or CLI):**

```json
{
  "family": "blog-api",
  "networkMode": "awsvpc",
  "containerDefinitions": [
    {
      "name": "blog-api",
      "image": "artenisal/blog-api:latest",
      "portMappings": [
        {
          "containerPort": 8000,
          "protocol": "tcp"
        }
      ],
      "environment": [
        {
          "name": "DATABASE_URL",
          "value": "postgresql://user:pass@rds-endpoint:5432/db"
        },
        {
          "name": "SECRET_KEY",
          "value": "your-secret-key"
        },
        {
          "name": "ENVIRONMENT",
          "value": "production"
        }
      ],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/blog-api",
          "awslogs-region": "us-east-1",
          "awslogs-stream-prefix": "ecs"
        }
      }
    }
  ],
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "256",
  "memory": "512"
}
```

**2. Create ECS Service with this task definition**

---

### Option D: Deploy to Google Cloud Run

```bash
# Tag for Google Container Registry
docker tag artenisal/blog-api:latest gcr.io/YOUR-PROJECT/blog-api

# Push to GCR
docker push gcr.io/YOUR-PROJECT/blog-api

# Deploy to Cloud Run
gcloud run deploy blog-api \
  --image gcr.io/YOUR-PROJECT/blog-api \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars "DATABASE_URL=postgresql://...,SECRET_KEY=..."
```

---

## Part 3: Environment Variables for Production

### Required Environment Variables:

```bash
# Database (use your production database URL)
DATABASE_URL=postgresql://user:password@host:5432/dbname

# Security (GENERATE A NEW SECRET!)
SECRET_KEY=your-super-long-random-secret-key-min-32-chars
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS (your frontend domain)
CORS_ORIGINS=https://yourdomain.com,https://www.yourdomain.com

# Environment
ENVIRONMENT=production
```

### Generate a Secure Secret Key:

```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

---

## Part 4: Database Setup

### Using AWS RDS PostgreSQL:

1. Create RDS PostgreSQL instance in AWS Console
2. Note the endpoint URL
3. Use this as your `DATABASE_URL`:
   ```
   postgresql://username:password@rds-endpoint.region.rds.amazonaws.com:5432/dbname
   ```

### Using Managed PostgreSQL (DigitalOcean, etc):

1. Create managed database
2. Get connection string
3. Use it as `DATABASE_URL`

### Run Migrations:

```bash
# SSH into your server or container
docker exec -it blog-api alembic upgrade head
```

---

## Part 5: Frontend Deployment

### Option A: Serve from Same Container

The frontend is already in the `frontend/` directory. You can serve it with nginx.

### Option B: Deploy to Netlify/Vercel (Recommended)

**Update `frontend/js/config.js`:**

```javascript
const API_BASE_URL = 'https://your-api-domain.com';  // Your production API
```

Then deploy the `frontend/` folder to Netlify or Vercel.

---

## Part 6: Post-Deployment Checklist

- [ ] Change all default passwords
- [ ] Set strong SECRET_KEY
- [ ] Configure CORS for your domain only
- [ ] Set up HTTPS (use Let's Encrypt or cloud provider SSL)
- [ ] Run database migrations
- [ ] Test all endpoints
- [ ] Set up monitoring (CloudWatch, Datadog, etc.)
- [ ] Configure backups for database
- [ ] Set up domain name and DNS
- [ ] Test user registration and login
- [ ] Create first admin user

---

## Part 7: Updating Your Deployment

### When you make code changes:

```bash
# 1. Build new version
docker build -t artenisal/blog-api:1.0.1 .

# 2. Push to Docker Hub
docker push artenisal/blog-api:1.0.1

# 3. Update production
docker-compose pull
docker-compose up -d

# Or if using ECS/Cloud Run, update the service to use new image version
```

---

## Part 8: Monitoring & Logs

### View Logs:

```bash
# Docker Compose
docker-compose logs -f api

# Single Container
docker logs -f blog-api

# AWS ECS
# Use CloudWatch Logs in AWS Console
```

### Health Check:

```bash
curl https://your-domain.com/health
# Should return: {"status":"healthy"}
```

---

## Part 9: Scaling

### Horizontal Scaling (More Containers):

```bash
# Docker Compose
docker-compose up -d --scale api=3

# ECS/Kubernetes
# Increase desired count in service configuration
```

### Vertical Scaling (More Resources):

Update container CPU/memory in your deployment configuration.

---

## Part 10: Troubleshooting

### Container won't start:

```bash
# Check logs
docker logs blog-api

# Common issues:
# - DATABASE_URL incorrect
# - SECRET_KEY not set
# - Port already in use
```

### Can't connect to database:

```bash
# Test connection
docker exec -it blog-api python -c "from app.core.database import engine; print(engine.url)"

# Check if database is reachable
docker exec -it blog-api ping postgres-host
```

### CORS errors in browser:

- Check `CORS_ORIGINS` environment variable
- Must include your frontend domain
- No trailing slashes

---

## 🎉 Congratulations!

Your 12 Factor Blog App is now deployed and running in production!

**Next Steps:**
- Monitor application logs
- Set up automated backups
- Configure monitoring alerts
- Add more features!

---

**Need help?** Check the main README.md or Docker/AWS documentation.
