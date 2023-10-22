# devops
Utility for monitoring memory on the device\API and docker-compose

## api_for_data_nosql
Create docker-compose.yml that deploys a python application with a simple REST API implementation. The solution should consist of two containers:
    
    a) Any NoSQL DB.

    b) A python application using Flask that listens on port 8080 and accepts only GET, POST, PUT methods.

    c) Create a value key=value, change key=new_value, read the value of the key.

    d) Newly created objects must be created, modified and read from the NoSQL DB.

## memory

Write a bash or python or groovy script that will monitor memory consumption and generate an alarm by sending an http request to the API.