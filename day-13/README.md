📦 Day 13 – Docker Compose

- On this day, I built a small full-stack setup to practice Docker Compose by running multiple services together.

- What I built:

A static HTML frontend served with Nginx (Created using ChatGPT only to run the code)

A PostgreSQL database (Created using ChatGPT only to run the code)

A FastAPI backend connected to the database (Created using ChatGPT only to run the code)

- Each service has its own Dockerfile, and everything is orchestrated using a single docker-compose.yml file.

- How it works

Docker Compose builds and starts all services with:

-- docker compose up --build --


When I needed to change exposed ports, I removed existing images and containers using:

-- docker compose down --rmi local -v --

- What I learned:

How to run multiple containers together using Docker Compose

How services communicate inside a Docker network

How to manage ports and rebuild images correctly

How to control containers and images from one central configuration file

- This project helped me understand how real-world applications combine frontend, backend, and database using Docker.