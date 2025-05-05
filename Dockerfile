
FROM python:3.12-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_PROJECT_ENVIRONMENT=/usr/local

RUN apt-get update && apt-get install --no-install-recommends -y \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* 

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Create a working directory
WORKDIR /app
# Copy the requirements file
COPY uv.lock pyproject.toml /app/

# Install the dependencies
RUN uv sync

COPY . /app/

ENV PYTHONPATH="/app"

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"

# ENV BASE_DIR="/app/rest_countries"

# Expose the port the app runs on
EXPOSE 8000

RUN chmod +x django_run.sh
# Set the entrypoint to the script
ENTRYPOINT ["/bin/bash", "./django_run.sh"]
# # Run the application
# CMD [ "python", f"{BASE_DIR}/manage.py", "runserver", "0.0.0.0:8000" ]