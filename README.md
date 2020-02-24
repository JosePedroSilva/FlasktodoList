# Barebones Flask To Do List

Structure of a to do list using Flask 
## Requirements
Python 3.6+, python-pip, virtualenv
## Getting Started

First, clone this repo

```
$ git clone https://github.com/JosePedroSilva/FlasktodoList 
$ cd FlasktodoList
```

Create virtual environment 

```
$ python3 -m venv env
$ source env/bin/activate
(env) $ _
```

Install all necessary dependencies

```
$ pip install -r requirements.txt
```
Set the flask environment
For windows use set command
```
(env) $ export FLASK_APP=microblog.py
```
Run the application:
```
(env) $ flask run
```
Access url to see web app
```
http://localhost:5000/
```