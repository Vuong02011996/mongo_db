# Install mongoDB on Docker
## With command line
ref: https://phoenixnap.com/kb/docker-mongodb

sudo docker pull mongo

sudo mkdir -p /mongodata

sudo docker run -it -v mongodata:/data/db -p 27017:27017 --name mongodb -d mongo
```commandline
-it – Provides an interactive shell to the Docker container.
-v – Use this option to attach the /mongodata host volume to the /data/db container volume.
-d – Starts the container as a background process.
--name – Name of the container.
```

sudo docker logs mongodb


## With docker-compose
https://www.osradar.com/deploy-mongodb-using-docker-compose/

https://yosh.ke.mu/mongo_in_docker

sudo docker-compose up -d   

## Start Interactive Docker Terminal (Bash Shell) to Manage MongoDB Database
sudo docker exec -it mongodb bash
```commandline
The MongoDB shell launches and the prompt is ready to accept your commands.
```

mongo -host localhost -port 27017 

```commandline
With the MongoDB shell, you can now create a database, add collections or manage individual documents.
```


# Install MongoDB Enterprise Edition on Ubuntu

# Basic using moongo

https://docs.mongoengine.org/guide/connecting.html


mongodb://root:example@14.241.120.239:11038/facial_recognition?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false