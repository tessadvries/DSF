#list of names and snacks
names = ["Tessa", "Manon", "Stijn"]
snacks = []

#loop through names and print name + amount of characters
for name in names:
	length = len(name)
	print("Hi " + name + "!" + " Your name has " + str(length) + " characters.")
	snack = input("What is your favorite snack? ")
	snacks.append(snack)

#combine name + favorite snack
index = 0
for name in names:
	snack = snacks[index]
	print("The favorite snack of " + name + " is: " + snack + ".")
	index += 1




