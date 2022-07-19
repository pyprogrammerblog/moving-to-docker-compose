# moving-to-docker-compose

Excellent!!

### Development

Clone the project and move inside
```shell
    git clone https://github.com/mopinion/moving-to-docker-compose.git
    cd moving-to-docker-compose
    docker-compose build
```
 
Install the virtualenv on the root project folder
```shell
    docker-compose run --rm --no-deps app poetry install
```

Finally, run the tests
```shell
    docker-compose run --rm app poetry run pytest
```
