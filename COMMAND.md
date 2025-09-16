# Get Stared

## Useful Commands

Bring containers up and build. Add -d flag to run output detached from current shell.

```bash
docker-compose up --build -d
```

Bring containers down. Add -v flag to also delete named volumes

```bash
docker-compose down -v
```

# Get Stared

## Useful Commands

Bring containers up and build. Add -d flag to run output detached from current shell.

```bash
docker-compose up --build -d
```

Bring containers down. Add -v flag to also delete named volumes

```bash
docker-compose down -v
```

Create superuser

```bash
docker-compose exec flask flask createsuperuser <email> <username>
```

Unittest

```bash
pytest
```

Coverage reports

```bash
coverage run -m pytest
coverage xml
```

Fixtures data seed

```bash
docker-compose exec flask flask seed
```

Redis

```bash
docker exec -it redis redis-cli

# GET
KEYS *
```