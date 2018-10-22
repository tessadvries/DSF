import requests

def api_call(title, value):
 	url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
 	req = requests.get(url)
 	data = req.json()
 	
 	if req.status_code != 200:
 		print("Error!")
 		exit()

 	if value == "description":
 		print(data["description"])

 	if value == "extract":
 		print(data["extract"])

 	return title, value

title = input("What would you like to read about? ").strip().replace(" ","_")
value = input("Would you like to read the extract or description? ").strip().lower()
data = api_call(title,value)

print(f'Here is the {value} for {title}')
api_call(title, value)