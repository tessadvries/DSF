import requests

#ask user for url
user_url = input("Please enter a URL: ").strip()
r = requests.get(user_url)

#check status code
if r.status_code != 200:
	print("Error!")
	exit()

#define and print headers
header = r.headers

for key, value in header.items():
	print(f'{key}: {value}')

#define and print text (first 10 lines)
text = r.text

index = 0
while index <= 10:
	line = text.splitlines()[index]
	print(line)
	index = index + 1
