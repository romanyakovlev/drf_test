from essential_generators import DocumentGenerator
import requests
import passgen
import random
import time
import json

with open("config.json") as json_data_file:
    data = json.load(json_data_file)

number_of_users = data['number_of_users']
max_posts_per_user = data['max_posts_per_user']
max_likes_per_user = data['max_likes_per_user']

gen = DocumentGenerator()

posts_counter = 0
user_tokens = []

for user in range(number_of_users):
	s = requests.Session()
	password = passgen.passgen()
	data = {"username": gen.phone(), "password1": password, "password2": password}
	r = s.post('http://127.0.0.1:8000/api/auth/registration/', data=data)
	token = r.json()['token']
	user_tokens.append(token)
	headers = {'Authorization':'JWT ' + token}
	for post in range(random.randint(1, max_posts_per_user)):
		data = {'text':gen.paragraph()}
		kek = requests.post('http://127.0.0.1:8000/api/posts/', headers=headers, data=data)
		posts_counter += 1

for token in user_tokens:
	s = requests.Session()
	headers = {'Authorization':'JWT ' + token}
	for post in range(random.randint(1, max_likes_per_user)):
		requests.get('http://127.0.0.1:8000/api/posts/{}/like/'.format(random.randint(1,posts_counter)), headers=headers)



