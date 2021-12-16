<!-- GETTING STARTED -->
## Getting Started

This is a project that changes the task status based on a predefined state machine that this task
must respect through APIs.

### How to run the project

1. You should have docker and docker-compose installed
2. Clone the repo
   ```sh
   git clone https://github.com/shroukhegazi/mentorship_project/
   ```
3. Go in directory at the same level of docker-compose
 
4. Build images
   ```sh
   docker-compose build 
   ```
5. Migrate models
   ```sh
   docker-compose run web python manage.py migrate
   ```
6. Run the project
   ```sh
   docker-compose up
   ```

# REST APIs FOR THIS PROJECT

This project consists of five APIs, They are described below.


## Get list of tasks

### Request

`GET /tasks/`

### URL
    http://127.0.0.1:8000/tasks/

### Response
    HTTP 200 OK
    Allow: POST, GET, OPTIONS
    Content-Type: application/json
    Vary: Accept

    []

## Create a new task

### Request

`POST /tasks/`

### URL 
    http://127.0.0.1:8000/tasks/

### Response

    HTTP/1.1 201 Created
    Allow: POST, GET, OPTIONS
    Content-Type: application/json
    Vary: Accept

    {"id":"1","title":"title","status":"Draft"}

## Get a specific task

### Request

`GET /tasks/pk`

### URL 
    http://127.0.0.1:8000/tasks/1

### Response

    HTTP 200 OK
    Allow: GET, PATCH, DELETE, OPTIONS
    Content-Type: application/json
    Vary: Accept


    {"id":1,"title":"title","status":"Draft"}


## Change the status of a task

### Request

`PATCH /tasks/pk`

### URL
    http://127.0.0.1:8000/task/1

### Response

    HTTP 200 OK
    Allow: OPTIONS, PATCH, DELETE, GET
    Content-Type: application/json
    Vary: Accept
    
    {"status": "Done"}
    

## Delete a specific task

### Request

`DELETE /tasks/pk`

### URL
    http://127.0.0.1:8000/tasks/1

### Response

    HTTP 204 No Content
    Allow: OPTIONS, PATCH, DELETE, GET
    Content-Type: application/json
    Vary: Accept




