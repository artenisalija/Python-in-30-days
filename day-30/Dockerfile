# Factor #5: Build, Release, Run - Strictly separate build and run stages

FROM python:3.11-slim as builder

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Final stage
FROM python:3.11-slim

WORKDIR /app

# Copy dependencies from builder
COPY --from=builder /root/.local /root/.local

# Copy application code
COPY ./app ./app
COPY ./alembic ./alembic
COPY ./alembic.ini .

# Make sure scripts in .local are usable
ENV PATH=/root/.local/bin:$PATH

# Factor #9: Disposability - Fast startup and graceful shutdown
# Factor #7: Port Binding - Export services via port binding
EXPOSE 8000

# Factor #11: Logs - Treat logs as event streams (stdout)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--log-level", "info"]
