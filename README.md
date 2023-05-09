# Yatube v.0.1.0 Community
Social network. 

[![CI](https://github.com/yandex-praktikum/hw02_community/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/yandex-praktikum/hw02_community/actions/workflows/python-app.yml)



## Features
- View Posts.


## History of Yatube project
- v.0.1.0 [Community] <- You are here

## Tech
- Python 3.9
- Django 2.2

#### Tested Python version
Python 3.7-3.9


## Installation (for Windows)
Clone repository
```sh
git clone git@github.com:KuzenkovAG/yatube_community.git
```
Install environment
```sh
python -m venv venv
```
Activate environment
```sh
source venv/Script/activate
```
Install requirements
```sh
pip install -r requirements.txt
```
Make migrations and run server
```sh
python manage.py migrate
```
Run server
```sh
python manage.py runserver
```

## Usage
Index page
```sh
http://127.0.0.1:8000/
```


Page of group (if group with slug=group_slug exists)
```sh
http://127.0.0.1:8000/group/group_slug/
```


## Author
[Alexey Kuzenkov]


   [Alexey Kuzenkov]: <https://github.com/KuzenkovAG>
   [Community]: <https://github.com/KuzenkovAG/yatube_community>