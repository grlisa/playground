# playground
In this playgrund repo I test and learn new technologies.
To have more practice with tools like FastAPI, SQLModel, Alembic, docker-compose, pytest, pre-commit, etc
the following development has been made:

- An API developed with FastAPI with 5 endpoints:
  - GET `/users`: To list all users in the db
  - POST `/users`: To add a new user specifying its email and role
  - GET `/users/{user_id}`: To get a specific user by its id
  - GET `/users/{user_id}/courses`: To get all the courses created by a specific user
  - GET `/courses`: To list all the courses
  - POST `/courses`: To add a new course specifying a user id of its owner
  - GET `/courses/{course_id}`: To get a speciific course by its id
  -
- A postgres DB with the tables **Course**, **User**, **Profile**, **Studentcourse** listening on port **5432**
- Migration with alembic

To use this project, with `docker-compose up` you will be able to run the service.
Once Its up and running, you can go to `localhost:8000/docs` to have access to the endpoints.
