---
layout: post
title:  "Docker Basics"
date:   2020-04-16 16:00:00 -0500
categories: Docker
---
# April 17th 2020
* * *
# Agenda
* Docker Basics
  * Installing Docker
  * Basic Docker Commands
  * Deploy a Basic Application

# Docker Basics

## Install Docker 

### Install for Docker Desktop for Windows or Mac  
Download the correct version of Docker Desktop for your system.  
`https://docs.docker.com/get-docker/`  

*If you have a Mac checkout installing it via HomeBrew! Windows can use Chocoately to do the same thing.*   


### Docker Architecture
Notice how the docker client communicates to the Docker Host. The Docker daemon/service downloads images from a registry and runs the containers on your system.  
![Docker Architecture Image](https://docs.docker.com/engine/images/architecture.svg)  

### Docker Engine
Docker engine is the main component that makes it all work. Docker is the CLI utility that you use to interact with the dockerd service that is exposed via a REST API.  
![Docker Engine](https://docs.docker.com/engine/images/engine-components-flow.png)  
  
### Docker Registries / Docker Hub  
A Docker registry stores Docker images. Docker Hub is a public registry that anyone can use, and Docker is configured to look for images on Docker Hub by default. You can also host your own private Docker repository using applications like Harbor. 
https://hub.docker.com/  
https://goharbor.io/  

## Basic Docker Commands

### Download an image from Docker Hub  
Now we will download an image from the docker hub repository by running the *pull* command.  
*Note: try pulling other images such as ubuntu or nginx*  
```
docker image pull centos
```

### Run a container interactively  
We can *run* a container and interact with it by specicfing the command to execute. What do you think the *-it* parmeter does? Check the help by running *docker run --help*.  
*Note: Try typing "hostname" or "ip address"; Type "exit" to quit.*  
```
docker run -it centos /bin/bash
```

### Run a container non-interactively (Detached)  
You most likely will want to run your containers in the background. You can do this by using the *-d* parameter.  
*Note: By adding the --name we assign our own name*    
```
docker run -d --name sleepy centos sleep 600
```

### List all containers  
Find your container by typing *docker ps*. Notice that you only see running containers. You can see all containers that have run by adding the *-a* parameter.  
*Note: Identify the container ID, status, command, and name of the container that you created*     
```
docker ps -a
```

### Connect to a running container
If you need to troubleshoot something inside of a container you can invoke a process inside of it. Lets start a container that runs a web server, and then open up a terminal to it through a second command.
```bash
#Run an nginx container
docker run -d --name web1 nginx

#Execute bash interactively
docker exec -it web1 /bin/bash

#Verify the nginx service is running
service nginx status
exit
```

### Deploy a basic web server
Lets now access our application by exposing the port that it is listening on by using the *-P* parameter.   
```bash  
#Runt he container and expose all ports
docker run -d -P --name  web2 nginx

#Identify the port and connect through a browser via http:#localhost:<port>
docker ps
```  

### Mount a folder to your container
Now we will take the nginx container and feed it a custom web page. Download the index.html file from the references section and save it to a folder.  
```bash
#Change the <folder> to the location you saved the index.html file
docker run -P --name myweb -v /<folder>:/usr/share/nginx/html:ro -d nginx

#Get the port of the container and connect to it
docker ps
```

### Stop and Delete a running or stopped container  
Delete the containers that we have created by running the below command.  
```bash
#Stop the container
docker stop <name>

#Delete the container
docker rm <name>
```

### Other Commands
The below snippet containers some other commands that you can try.
```bash
#Remove all images, containers, volumes, and networks.
docker system prune

#List Images
docker images ls

#Delete an Image
docker image rm <image_name> 
docker rmi <image_name>

#Remove all Images
docker rmi $(docker images -a -q)
```

* * *

# Bonus
## Homebrew  
**This missing package manager for macOS!** 

1. Install HomeBrew by running the below command in a terminal.  
`/bin/bash -c "$(curl -fsSL https:#raw.githubusercontent.com/Homebrew/install/master/install.sh)"`
2. Install Docker Desktop via HomeBrew  
`brew install docker docker-machine`

* * *

# References
* Docker Getting Started - https://docs.docker.com/get-started/overview/
* Demo Static Web Page - https://raw.githubusercontent.com/168cyber/168cyber.github.io/master/files/docker-basics/index.html