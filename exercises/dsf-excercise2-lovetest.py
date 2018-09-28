#LOVETEST | DSF

# asking for names
name1 = input("What is your name? ")
name2 = input("What is your partners name? ")

#lowercase and strip the names
name1 = name1.strip().lower()
name2 = name2.strip().lower()

print("Calculating: " + name1 + " vs. " + name2)

#this is the basic part of the excercise:
#if name1 == name2:
#	print("You have the same name, that is strange!")
#elif name1 < name2:
#	print("Perfect match!")
#elif name1 > name2:
#	print("Not so great of a match!")

#calculation based on lenght of the names
count_name_1 = len(name1)
count_name_2 = len(name2)
count_dif = abs(count_name_1 - count_name_2)

if count_dif == 0:
	print("You are a 100% match")
elif count_dif == 1:
	print("You are a 80% match")
elif count_dif == 2:
	print ("You are a 60% match")
elif count_dif == 3:
	print ("You are a 40% match")
elif count_dif == 4:
	print ("You are a 20% match")
else:
	print ("we recommend you find somebody else")

