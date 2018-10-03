calories = 189
fat = 7.7
carbs = 13.4
sugar = 14.7
fiber = 0.6
salt = 0.26
protein = 1.5

amount = input("how many stroopwafels have you had today?")

print("You had " + amount + " stroopwafels today")

amount = float(amount)

user_calories = calories * amount
user_fat = fat * amount
user_carbs = carbs * amount
user_sugar = sugar * amount
user_fiber = fiber * amount
user_salt = salt * amount
user_protein = protein * amount

print("Calories consumed: " + str(user_calories) + " calories")
print("Fat consumed: " + str(user_fat) + " grams")
print("Carbs consumed: " + str(user_carbs) + " grams")
print("Sugar consumed: " + str(user_sugar) + " grams")
print("Fiber consumed: " + str(user_fiber) + " grams")
print("Salt consumed: " + str(user_salt) + " grams")
print("Protein consumed: " + str(user_protein) + " grams")
