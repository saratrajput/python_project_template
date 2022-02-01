# Python Project Template
This is a simple template to get started on your python projects.

**NOTE:**The template installs opencv modules for demonstration purposes.

## How To Use This Template
* Install cookiecutter
```
pip install cookiecutter
```

* Setup the template with cookiecutter.
```
cookiecutter "repo_addr"
```

## Directory Structure
```
.
├── Dockerfile
├── images
├── README.md
├── requirements.txt
└── scripts
    └── main.py
```

## Things included
* Directory structure.
* A simple script with boilerplate for:
    * Argument Parsing.
    * Logging.
* **requirements.txt** to list the requirements.
* **Dockerfile** to containerize your project.


## How To Contribute
* Feel free to customize the template as per your liking in a separate branch.
```
git clone <repo>
git branch <custom-template>
git checkout <custom-template>
# Make changes, commit and push
```

* You can now create your custom template projects with:
```
cookiecutter -c <custom-template> repo
```

