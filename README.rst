# Test

Excellent!!

### Deployment

This is a minimal way of deployment on the server.

1. For deployment:

```shell
    git clone https://github.com/mopinion/moving-to-docker-compose.git
    cd moving-to-docker-compose
    docker-compose build app
    docker-compose run --rm --no-deps app poetry install --deploy --dev
    docker-compose up -d --no-deps app
```
