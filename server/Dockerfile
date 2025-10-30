# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3-slim

EXPOSE 5000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat-openbsd build-essential && \
    rm -rf /var/lib/apt/lists/*


WORKDIR /app
COPY . /app

# Install pip requirements
RUN pip install -r requirements/local.txt

# Make entrypoints executable
RUN chmod +x ./scripts/migrate.entrypoint.sh
RUN sed -i 's/\r$//g' ./scripts/migrate.entrypoint.sh

ENTRYPOINT ["./scripts/migrate.entrypoint.sh"]

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "app.py"]
