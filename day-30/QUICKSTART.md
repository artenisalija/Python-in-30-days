# Quick Start Guide - 5 Minutes to Running App! ⚡

## Step 1: Copy Environment File
```bash
cp .env.example .env
```

## Step 2: Start Everything
```bash
docker-compose up --build
```

Wait 30-60 seconds for everything to start...

## Step 3: Access the App

✅ **Frontend**: http://localhost:3000  
✅ **API Docs**: http://localhost:8000/docs  
✅ **API**: http://localhost:8000  

## Step 4: Create Your First User

1. Go to http://localhost:3000
2. Click **"Register"**
3. Fill in:
   - Email: `test@example.com`
   - Username: `testuser`
   - Password: `password123`
4. Click **"Register"**
5. Click **"Sign in"** and login
6. Click **"New Post"** to create your first blog post!

---

## That's It! 🎉

You now have a fully functional 12 Factor blog application running!

### What's Running?

- **PostgreSQL Database** on port 5432
- **FastAPI Backend** on port 8000
- **Frontend** on port 3000

### Stopping the App

```bash
# Stop all services
docker-compose down

# Stop and remove volumes (clean slate)
docker-compose down -v
```

### Restarting

```bash
# Start services again
docker-compose up

# Or in background
docker-compose up -d
```

---

## Next Steps

1. **Explore the API**: Visit http://localhost:8000/docs
2. **Create posts**: Login and start blogging!
3. **Check the code**: See how a 12 Factor app works
4. **Deploy it**: Push to Docker Hub and deploy anywhere!

---

## Need Help?

- Check the main **README.md** for detailed documentation
- View logs: `docker-compose logs -f`
- Restart services: `docker-compose restart`

---

**Enjoy your 12 Factor Blog App!** 🚀
