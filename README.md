# Microservices coppel test

Microservices coppel test.

Please provide os variables environtment

```
/docker-compose.yaml
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
pipenv run start
```

## Dev enviroment using docker 🐋

```
docker-compose -f docker-compose-dev.yaml build
docker-compose -f docker-compose-dev.yaml up -d

docker exec -it server-container pipenv run start
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
