#open footballers csv file
f = open("footballers.csv")
newfile = open("new_footballers.txt", "w")

footballers = []

#loop over the lines using a for loop, and print a new sentence
#create and write new file
for line in f:
	row = line.strip().split(",")
	footballers.append(row)
	player = row[0]
	club = row[1]
	amount = row[2]
	print(player + " went to " + club + " for " + amount + " million euros.")
	newfile.write(player + " transferred to " + club + " for " + amount + ".000.000 million euros." + "\n")

#add extra football
player = input("Please enter the players name: ")
club = input("Please enter the new club: ")
amount = input("Please enter the amount the player is sold for (in millions): ")

new_row = player + " is sold to " + club + " for " + amount + " euros."
newfile.write(new_row)

#close the files
f.close()
newfile.close()
