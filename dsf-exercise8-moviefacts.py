facts = {
		"title" : "London Has Fallen",
		"release year" : 2016,
		"duration" : 99,
		"director" : "Babak Najafi"
		}

facts["actors"] = "Gerard Butler", "Aaron Eckhart"

for key, value in facts.items():
	if key == "duration":
		print(f'{key}: {value} minutes')
	elif key == "actors":
		print(key + ": " + ", ".join(value))
	else:
		print(f'{key} : {value}')
	
