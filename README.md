# API Webserver Project

## **How To Run the Application**

- Please git clone this project
- Please add one feature and make subsequent pushes feature by feature
- After pushing the changes please make a pull request
- When making each push please mention in the README file what feature has been added and how the code needs to run
- I have created a src folder, keep all the source code of the project inside the src folder except files like README.md, .gitignore and requirements.txt
- Tools to check out for creating the ERD diagram https://dbdiagram.io/home and https://www.lucidchart.com/pages/
- Also really important, don't forget "All queries to the database must be commented with an explanation of how they work and the data they are intended to retrieve"

To install and run this application you need:

- Python 2.7 or 3.3+
- virtualenv (not required if you are using Python 3.4)
- git (only to clone this repository)

Installation
------------

The commands below install the application and its dependencies:

    $ virtualenv venv
    $ . venv/bin/activate
    (venv) pip install -r requirements.txt

Note for Python 3.4 users: replace `virtualenv` with `pyvenv`.

Note for Microsoft Windows users: replace the virtual environment activation command above with `venv\Scripts\activate`.

Running
-------

```
#start web server
flask run
```

# The app will run on : [localhost:5000 ](localhost:5000 "localhost:5000")
