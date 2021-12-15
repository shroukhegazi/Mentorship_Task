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
