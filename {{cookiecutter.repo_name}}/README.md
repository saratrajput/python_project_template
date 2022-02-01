# {{cookiecutter.project_name}}
This README would normally document whatever steps are necessary to get your application up and running.

[How to use Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#headers)

## Requirements
List the requirements for the repo.
* Python
* OpenCV
```
pip install -r requirements.txt
```

## Setup
List the steps needed to install this project.

### Docker
* Build docker container.
```
docker build -t {{cookiecutter.repo_name}} .
```

* Run container with interactive shell.
```
docker run -it --rm {{cookiecutter.repo_name}}:latest bash
```

* Inside docker container
```
cd home/scripts/
python3 main.py
```

### Summary of set up
* Configuration
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

### Contribution guidelines
* Writing tests
* Code review
* Other guidelines

### Who do I talk to?
* Repo owner or admin: {{cookiecutter.author}}
* Other community or team contact
