# Microservices coppel test

Microservices coppel test.

Please provide os variables environment using the following file

```
./docker-compose.yaml
```

## Deployment

```
docker-compose pull
docker-compose up -d
```

## Dev enviroment using python 📦

```
cd server
pipenv install
pipenv run start_users
pipenv run start_characters
pipenv run start_comics
```

## Dev enviroment using docker 🐋

```
docker-compose -f docker-compose-dev.yaml build
docker-compose -f docker-compose-dev.yaml up -d

docker exec -it users-container pipenv run start_users
docker exec -it characters-container pipenv run start_characters
docker exec -it comics-container pipenv run start_comics
```

## Open your browser 🚀

[localhost:5000](http://localhost:5000)
[localhost:5001](http://localhost:5001)
[localhost:5002](http://localhost:5002)

## Devs ✒️

* **Jesús Alejandro Yahuitl Rodríguez** - *Dev* - [YisusYaro](https://github.com/YisusYaro/)


## License 📄

This project is under the License described in the file [LICENSE](LICENSE)

---
⌨️ with ❤️
