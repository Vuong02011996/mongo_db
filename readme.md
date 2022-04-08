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
          - /home/vuong/Desktop/services/mongoDB/mongodb:/data/db
    ```
+ Run command: *sudo docker-compose up -d*


# Install MongoDB Enterprise Edition on Ubuntu(GUI mongodb)
+ Reference in [the-best-mongodb-guis-in-2020](https://retool.com/blog/the-best-mongodb-guis-in-2020/)
+ Can use : Mongo Compass, Robo 3T, ...

**Compass**
+ connect: ```mongodb://root:example@localhost:11038```

**Robo 3T**
  
+ Install : sudo snap install robo3t-snap

# Basic using mongo with python.
+ ORM
  + Object-Relational Mapping (ORM) is a technique that lets you query and manipulate data from a database using an object-oriented paradigm.
  + [ORM of mongoDB](https://pymongo.readthedocs.io/en/stable/tools.html#orm-like-layers)
  + [orm-mongoengine](https://github.com/mongoengine/mongoengine)
+ In python you can use pymongo or mongoengine.
+ Some benchmarking compare pymongo and mongoengine:
  + [Q Tai](https://docs.google.com/document/d/1h61YLduQt4_tvU9MGXbOp4tth5TBOizd2iR57F8N7pg/edit)
  + [stackoverflow](https://stackoverflow.com/questions/35257305/mongoengine-is-very-slow-on-large-documents-compared-to-native-pymongo-usage)
+ Reference 
  + [mongodb](https://docs.mongodb.com/manual/crud/)
  + [pymongo](https://pymongo.readthedocs.io/en/stable/tutorial.html) 
  + [mongoengine](https://docs.mongoengine.org/guide/defining-documents.html)
  + [video-tutorial-mongoengine](https://github.com/parisnakitakejser/video-tutorial-python-code/tree/master/mongoengine)


# Error
+ pymongo.errors.OperationFailure: Authentication failed.
  * check your path mongodb in volumes docker compose.
# Note abc
