
# Things I have done in Assignment

- Implemented all the missing APIs.
- Increase pyTest test coverage to maximum as I can and I got 95% test coverage in the pyTest.

![all pass](https://user-images.githubusercontent.com/52989607/196522519-31fdbe27-42e0-4aed-8d00-5cbfc842f79f.png)


# Missing APIs

- Grade an Assignment
- List all Assignments that is submitted to the particular teacher.

# New Files

- Dockerfile
- docker-compose.yml

# Errors

when I copy files from directory to image and installing the requirements file throw error which i have mentioned below 


```
 => [ 9/10] RUN chmod 777 venv                                                                                                                                                                 0.5s 
 => ERROR [10/10] RUN . venv/bin/activate && pip install -r requirements.txt                                                                                                                   1.5s 
------
 > [10/10] RUN . venv/bin/activate && pip install -r requirements.txt:
#0 1.347 ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requirements.txt'
------
failed to solve: executor failed running [/bin/sh -c . venv/bin/activate && pip install -r requirements.txt]: exit code: 1
```

so to solve this i have used the git repo URL to fetch the project and then make it as WORKDIR and install all dependencies.

## Requirements

- Docker

## Installation

Clone this project

Go to the project directory

hit given commands.

```bash
$ cd fly-backend/
$ docker-compose up
```
Now Application is ready to use

Just open browser and type and hit enter
```
http://127.0.0.1:8000/
```
# Tools that I use to test APIs

- [RapidAPI](https://rapidapi.com/)
