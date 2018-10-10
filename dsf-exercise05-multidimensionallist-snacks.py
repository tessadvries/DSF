friends = [
    ["Tessa"],
    ["Stijn"],
    ["Manon"]
]

for friend in friends:
    name = friend[0]
    length = len(name)
    print(name + ". This name has " + str(length) + " characters.")
    snack = input("What is your favorite snack? ")
    friend.append(snack)

for friend in friends:
  print("The favorite snack of " + friend[0] + " is" + " " + friend[1])
