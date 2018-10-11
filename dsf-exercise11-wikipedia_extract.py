import requests
import json


user_article = input("Please enter the name of the Wikipedia article you would like to see: ").strip().replace(" ","_")
language = ["nl", "en", "es"]

for item in language:
	url = f"https://{item}.wikipedia.org/api/rest_v1/page/summary/{user_article}"
	r = requests.get(url)

	if r.status_code != 200:
		print("Error!")
		exit()

	data = json.loads(r.text)

	title = data["title"]
	description = data["description"]
	extract = data["extract"]

	print(f'\n{item.upper()}')
	print(f'Title: {title}')
	print(f'Description: {description}')
	print(f'Extract: {extract}')