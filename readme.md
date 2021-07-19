# Install mongoDB Server
## Using docker image
+ Reference: [here](https://phoenixnap.com/kb/docker-mongodb)
+ Install:

    ```
    sudo docker pull mongo
    sudo mkdir -p /mongodata
    sudo docker run -it -v mongodata:/data/db -p 27017:27017 --name mongodb -d mongo
        -it – Provides an interactive shell to the Docker container.
        -v – Use this option to attach the /mongodata host volume to the /data/db container volume.
        -d – Starts the container as a background process.
        --name – Name of the container.
    sudo docker logs mongodb
    ```




## With docker-compose
*Remember that installing it this way is recommended for servers and production systems and not so much for development.*

[link1 Deploy mongo using docker compose](https://www.osradar.com/deploy-mongodb-using-docker-compose/)

[link2 Mongo in docker compose](https://yosh.ke.mu/mongo_in_docker)

+ Create folder to save file dockers-compose and database.
+ Create file docker-compose.yaml and add the following content:
    ```
    version: '3'
    
    services:
      mongodb:
        image: 'mongo:latest'
        environment:
          MONGO_INITDB_ROOT_USERNAME: root
          MONGO_INITDB_ROOT_PASSWORD: example
        ports:
          - 11038:27017
        restart: always
        volumes:
          - /workspace/services/databases/mongodb:/data/db
    ```
+ Run command: *sudo docker-compose up -d*   

## Start Interactive Docker Terminal (Bash Shell) to Manage MongoDB Database

sudo docker exec -it mongodb bash
```commandline
The MongoDB shell launches and the prompt is ready to accept your commands.
```

mongo -host localhost -port 27017 

```commandline
With the MongoDB shell, you can now create a database, add collections or manage individual documents.
```


# Install MongoDB Enterprise Edition on Ubuntu(GUI mongodb)
+ Reference in [here](https://retool.com/blog/the-best-mongodb-guis-in-2020/)
+ Can use : Mongo Compass, Robo 3T, ...

**Compass**
+ connect: ```mongodb://root:example@localhost:11038```

**Robo 3T**
  
+ Install : sudo snap install robo3t-snap

# Basic using mongo

+ Reference in [here](https://github.com/parisnakitakejser/video-tutorial-python-code/tree/master/mongoengine)

https://docs.mongoengine.org/guide/connecting.html
