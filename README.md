# drf_test


# What is it

Test task for company

# Requirements

- Django
- DRF

# How to use guide

1. Install dependencies
```
$ pip install -r requirements.txt
```
2. Make database migrations 
```
$ python manage.py runserver
```

3. Generate test data using python script
```
$ python data_fill_script.py
```

4. run django app
```
$ python manage.py runserver
```

Authorization in Django app is provided by JWT token. REST API is build using DRF.
API examples and token authorization are shown in data_fill_script.py script.
Main api requests are shown below:


```
- [POST] api/auth/registration/ # register new user
- [GET] api/users/ # users list
- [GET] api/users/<:pk>/ # user data
- [GET] api/users/<:pk>/activity/ # activity about <:pk> user
- [GET] api/posts/ # posts list
- [POST] api/posts/ # post create
- [PUT] api/posts/<:pk> # post edit
- [POST] api/posts/<:pk>/like/ # post like
- [POST] api/posts/<:pk>/dislike/ # post dislike
- [GET] api/analitics/ # analitics about authenticated user
```
