# Day 30 - 12 Factor Blog Application

A complete 12 Factor Blog API built with FastAPI, PostgreSQL, and a simple HTML/CSS/JS frontend with Tailwind CSS.

## 🎯 12 Factor App Implementation

This application demonstrates all 12 factors of a cloud-native application:

### 1. **Codebase** ✅
- Single codebase tracked in version control
- One app, many deploys (dev, staging, production)
- Located: Entire repository

### 2. **Dependencies** ✅
- Explicitly declare all dependencies
- Never rely on system packages
- Located: `requirements.txt`

### 3. **Config** ✅
- Store configuration in environment variables
- Never hardcode secrets or environment-specific values
- Located: `.env.example`, `app/core/config.py`

### 4. **Backing Services** ✅
- Treat databases as attached resources
- Can swap PostgreSQL instance via DATABASE_URL
- Located: `docker-compose.yml`, `app/core/database.py`

### 5. **Build, Release, Run** ✅
- Strict separation of build and run stages
- Build: `docker build`
- Release: Tagged Docker image
- Run: `docker run` or `docker-compose up`
- Located: `Dockerfile`

### 6. **Processes** ✅
- Execute app as stateless processes
- No in-memory session state
- All data stored in PostgreSQL
- Located: `app/main.py`, database sessions

### 7. **Port Binding** ✅
- Export HTTP service via port binding
- Self-contained, doesn't depend on external web server
- Located: `Dockerfile` (EXPOSE 8000), `app/main.py` (Uvicorn)

### 8. **Concurrency** ✅
- Scale out via the process model
- Can run multiple worker processes
- Located: `docker-compose.yml` (workers configuration)

### 9. **Disposability** ✅
- Fast startup and graceful shutdown
- Maximize robustness
- Located: `app/main.py` (startup/shutdown events), `Dockerfile`

### 10. **Dev/Prod Parity** ✅
- Keep development and production as similar as possible
- Same database (PostgreSQL) in all environments
- Located: `docker-compose.yml`

### 11. **Logs** ✅
- Treat logs as event streams
- Write to stdout, never manage log files
- Located: `app/main.py` (logging configuration)

### 12. **Admin Processes** ✅
- Run admin tasks as one-off processes
- Database migrations using Alembic
- Located: `alembic/`, migration commands

---

## 🚀 Quick Start

### Prerequisites
- Docker and Docker Compose installed
- Git (optional)

### 1. Clone or Download the Project

```bash
# If using git
git clone <repository-url>
cd day-30

# Or just extract the downloaded zip file
```

### 2. Set Up Environment Variables

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env if needed (default values work for local development)
```

### 3. Start the Application

```bash
# Build and start all services
docker-compose up --build

# Or run in detached mode
docker-compose up -d --build
```

This will start:
- **PostgreSQL** on port 5432
- **FastAPI backend** on port 8000
- **Frontend** on port 3000

### 4. Access the Application

- **Frontend**: http://localhost:3000
- **API Documentation**: http://localhost:8000/docs
- **API Root**: http://localhost:8000

### 5. Create Your First User

1. Go to http://localhost:3000
2. Click "Register"
3. Fill in the form
4. Login with your credentials
5. Start creating blog posts!

---

## 📁 Project Structure

```
day-30/
├── app/                          # FastAPI application
│   ├── api/                      # API endpoints
│   │   ├── auth.py              # Authentication routes
│   │   ├── posts.py             # Blog post routes
│   │   └── comments.py          # Comment routes
│   ├── core/                    # Core functionality
│   │   ├── config.py           # Configuration (Factor #3)
│   │   ├── database.py         # Database connection (Factor #4)
│   │   └── security.py         # JWT & password hashing
│   ├── models/                  # SQLAlchemy models
│   │   ├── user.py             # User model
│   │   ├── post.py             # Post model
│   │   └── comment.py          # Comment model
│   ├── schemas/                 # Pydantic schemas
│   │   ├── user.py             # User schemas
│   │   ├── post.py             # Post schemas
│   │   └── comment.py          # Comment schemas
│   └── main.py                  # FastAPI app entry point
├── alembic/                     # Database migrations (Factor #12)
│   ├── versions/               # Migration files
│   ├── env.py                  # Alembic environment
│   └── script.py.mako         # Migration template
├── frontend/                    # Simple HTML/CSS/JS frontend
│   ├── css/
│   │   └── style.css          # Custom styles
│   ├── js/
│   │   ├── config.js          # API configuration
│   │   ├── auth.js            # Authentication helpers
│   │   ├── login.js           # Login page
│   │   ├── register.js        # Registration page
│   │   ├── index.js           # Home page
│   │   ├── post.js            # Single post view
│   │   └── create-post.js     # Create post page
│   ├── index.html             # Home page
│   ├── login.html             # Login page
│   ├── register.html          # Registration page
│   ├── create-post.html       # Create post page
│   └── post.html              # Single post view
├── tests/                       # Unit tests
├── Dockerfile                   # Docker image (Factor #5)
├── docker-compose.yml          # Multi-service setup (Factor #10)
├── requirements.txt            # Python dependencies (Factor #2)
├── alembic.ini                 # Alembic configuration
├── .env.example                # Environment template (Factor #3)
└── README.md                   # This file
```

---

## 🔧 Development

### Running Locally Without Docker

1. **Install Python dependencies:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. **Start PostgreSQL** (you'll need it running locally or via Docker)

3. **Set environment variables:**
```bash
export DATABASE_URL="postgresql://bloguser:blogpassword@localhost:5432/blogdb"
export SECRET_KEY="your-secret-key"
```

4. **Run migrations:**
```bash
alembic upgrade head
```

5. **Start the application:**
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

6. **Serve frontend** (use any static server or open index.html)

### Database Migrations

**Create a new migration:**
```bash
docker-compose exec api alembic revision --autogenerate -m "Description"
```

**Apply migrations:**
```bash
docker-compose exec api alembic upgrade head
```

**Rollback migration:**
```bash
docker-compose exec api alembic downgrade -1
```

### Running Tests

```bash
# Run tests inside container
docker-compose exec api pytest

# Or locally
pytest
```

---

## 🌐 API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login (get JWT token)
- `GET /api/auth/me` - Get current user

### Posts
- `GET /api/posts/` - List all posts
- `GET /api/posts/{id}` - Get specific post with comments
- `POST /api/posts/` - Create new post (requires auth)
- `PUT /api/posts/{id}` - Update post (requires auth, owner only)
- `DELETE /api/posts/{id}` - Delete post (requires auth, owner only)
- `GET /api/posts/user/{user_id}` - Get posts by user

### Comments
- `GET /api/comments/post/{post_id}` - Get comments for post
- `POST /api/comments/` - Create comment (requires auth)
- `DELETE /api/comments/{id}` - Delete comment (requires auth, owner only)

### Health Check
- `GET /health` - Health check endpoint

Full API documentation available at: http://localhost:8000/docs

---

## 🐳 Docker Hub Deployment

### 1. Build the Image

```bash
docker build -t your-dockerhub-username/blog-api:1.0.0 .
```

### 2. Test Locally

```bash
docker run -p 8000:8000 \
  -e DATABASE_URL="postgresql://user:pass@host:5432/db" \
  -e SECRET_KEY="your-secret-key" \
  your-dockerhub-username/blog-api:1.0.0
```

### 3. Push to Docker Hub

```bash
# Login to Docker Hub
docker login

# Push the image
docker push your-dockerhub-username/blog-api:1.0.0

# Tag as latest (optional)
docker tag your-dockerhub-username/blog-api:1.0.0 your-dockerhub-username/blog-api:latest
docker push your-dockerhub-username/blog-api:latest
```

### 4. Deploy Anywhere

```bash
# Pull and run from any machine
docker pull your-dockerhub-username/blog-api:1.0.0
docker run -p 8000:8000 \
  -e DATABASE_URL="your-production-db-url" \
  -e SECRET_KEY="your-production-secret" \
  your-dockerhub-username/blog-api:1.0.0
```

---

## 🔒 Security Notes

### For Production:

1. **Change the SECRET_KEY:**
```bash
# Generate a secure secret key
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

2. **Use strong database credentials:**
- Don't use default passwords
- Use environment variables, never hardcode

3. **Enable HTTPS:**
- Use a reverse proxy (nginx, Traefik)
- Get SSL certificates (Let's Encrypt)

4. **Set CORS properly:**
- Only allow your frontend domain
- Never use `*` in production

5. **Use environment-specific configs:**
- Different `.env` for dev, staging, production
- Use secret management tools (AWS Secrets Manager, HashiCorp Vault)

---

## 🎨 Frontend Features

- **Responsive Design**: Works on mobile, tablet, and desktop
- **Modern UI**: Built with Tailwind CSS
- **JWT Authentication**: Secure token-based auth
- **Real-time Updates**: Fetch latest posts and comments
- **User-friendly**: Clean, intuitive interface

---

## 📊 Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **PostgreSQL** - Reliable relational database
- **SQLAlchemy** - ORM for database operations
- **Alembic** - Database migration tool
- **Pydantic** - Data validation
- **JWT** - Secure authentication
- **Uvicorn** - ASGI server

### Frontend
- **HTML5** - Structure
- **Tailwind CSS** - Styling
- **Vanilla JavaScript** - Interactivity
- **Fetch API** - API calls

### DevOps
- **Docker** - Containerization
- **Docker Compose** - Multi-container orchestration

---

## 🐛 Troubleshooting

### Database Connection Issues

```bash
# Check if PostgreSQL is running
docker-compose ps

# Check logs
docker-compose logs postgres

# Restart services
docker-compose restart
```

### Port Already in Use

```bash
# Find what's using the port
# Linux/Mac:
lsof -i :8000

# Windows:
netstat -ano | findstr :8000

# Change ports in docker-compose.yml if needed
```

### Frontend Can't Reach API

- Check CORS settings in `app/main.py`
- Verify API is running on port 8000
- Check browser console for errors
- Ensure `frontend/js/config.js` has correct API URL

---

## 📝 License

This is a learning project for Day 30 of your development journey.

---

## 🎓 Learning Resources

- [12 Factor App Methodology](https://12factor.net/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Docker Documentation](https://docs.docker.com/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Tailwind CSS](https://tailwindcss.com/)

---

## 🚀 Next Steps

1. **Add Features:**
   - Post categories/tags
   - User profiles
   - Post likes
   - Search functionality
   - Image uploads

2. **Improve Security:**
   - Rate limiting
   - Email verification
   - Password reset
   - Two-factor authentication

3. **Deploy to Cloud:**
   - AWS ECS/EKS
   - Google Cloud Run
   - Heroku
   - DigitalOcean

4. **Add Monitoring:**
   - Application logs
   - Performance metrics
   - Error tracking (Sentry)
   - Health checks

---

## ✅ Day 30 Complete!

You've built a production-ready 12 Factor application! 🎉

**What you learned:**
- All 12 factors of cloud-native apps
- FastAPI development
- JWT authentication
- PostgreSQL with SQLAlchemy
- Docker containerization
- Frontend integration
- REST API design

**Ready for deployment to Docker Hub and cloud platforms!**
