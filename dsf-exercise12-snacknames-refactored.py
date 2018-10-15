friends = {
	"Tessa" : " ",
	"Manon" : " ",
	"Stijn" : " ",
}

for key in friends:
	length = len(key)
	print(f'Hi {key}! Your name has {length} characters.')
	friends[key] = input(f'{key}, what is your favorite snack? ')
	value = friends[key]

print(friends)

for key, value in friends.items():
	print(f'The favorite snack of {key} is {value}')