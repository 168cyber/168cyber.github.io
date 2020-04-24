---
layout: post
title:  "Ride The ELK"
date:   2020-04-24 05:00:00 -0500
categories: ['Elasticsearch', 'Logstash', 'Kibana', 'Basics',]
tags: ['ELK']
---
# April 24th 2020
* * *
![Docker Architecture Image](https://skillvalue.com/jobs/wp-content/uploads/sites/7/2019/10/elk-developer-part-time-job-remote-project.jpg)
# Ride The ELK
**Topics**
  * Running ELK Docker
  * Kibana Dev Tools / Mapping Your Data
  * Ingesting Data
  * Grooming Data with Python 3

# ELK Prerequisites 
* Virtual Machine with 6GB of RAM (Ubuntu 18 Server preferred)
* Docker Installed
* Install docker-compose
* Host --> VM communication (Kibana)
* Python 3 & IDE (optional)
## Install Docker & Docker-Compose

**Install for Docker Desktop for Windows or Mac**  
`https://docs.docker.com/get-docker/`

**Docker-Compose**
`$ sudo curl -L "https://github.com/docker/compose/releases/download/1.25.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`
`$ sudo chmod +x /usr/local/bin/docker-compose`
`$ sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose`

**Git Clone the repo files**
`git clone https://github.com/168cyber/168cyber.github.io.git`
*This will have all the config files and commands referenced in the chat*

**Grab Container**
`$ sudo docker pull sebp/elk`

**Give ELK Docker Additional Memory**
`sudo sysctl -w vm.max_map_count=262144`

**Finally Spin up the ELK Docker**
`$ sudo docker-compose up elk-test` (*ensure you're in the right directory to grab the docker-compose.yml file*)



# References
* ELK Docker Docs - [https://elk-docker.readthedocs.io/](https://elk-docker.readthedocs.io/)
* Geo-point  Elasticsearch - [https://www.elastic.co/guide/en/elasticsearch/reference/current/geo-point.html](https://www.elastic.co/guide/en/elasticsearch/reference/current/geo-point.html)
* Date Elasticsearch - [https://www.elastic.co/guide/en/elasticsearch/reference/current/date.html](https://www.elastic.co/guide/en/elasticsearch/reference/current/date.html)
* JSON Beautifier - [https://codebeautify.org/jsonviewer](https://codebeautify.org/jsonviewer)
