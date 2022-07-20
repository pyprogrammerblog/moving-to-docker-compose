# moving-to-docker-compose

Excellent!!

### Development

Clone the project and move inside:
```shell
git clone https://github.com/mopinion/moving-to-docker-compose.git
cd moving-to-docker-compose
```
 
Install the virtualenv on the root project folder:
```shell
docker-compose run --rm --no-deps app poetry install
```

Check your installed dependencies for security vulnerabilities
```shell
docker-compose run --rm app poetry check
```

Finally, run the tests:
```shell
docker-compose run --rm app poetry run pytest
```
