import json

#open json database
with open("movies.json") as f:
	movies = json.load(f)

#ask for year
input_year = int(input("From what year would you like to see the movies in the database?: "))

#loop through years
for movie in movies:
	year = movie["year"]
	title = movie["title"]
	if year == input_year:
		print(f'The movie {title} is from {year}')

#supply several options to filter through database
print("If you would like to filter differently please choose one of the following options: ")
print("1: Search for movies based on duration")
print("2: Search for movies based on director")
print("3: Search for movies based on genres")
print("4: Search for movies based on actors")
user_option = input("Please enter your choice: ")

#duration 
if user_option == "1":
	movie_duration = int(input("The film has to be how many minutes or longer? "))
	for movie in movies:
		duration = movie["duration"]
		title = movie["title"]
		if duration >= movie_duration:
			print(f'{title} is {duration} minutes.')

#director
if user_option == "2":
	movie_director = input("Please enter a directors name ")
	for movie in movies:
		director = movie["director"]
		title = movie["title"]
		if director == movie_director:
			print(f'{title}.')	

#genres (use in because genres is a list)
if user_option == "3":
	movie_genre = input("Please enter the genre you are looking for ")
	for movie in movies: 
		title = movie["title"]
		genres = movie["genres"]
		if movie_genre in genres:
			print(f'{title}.')

#actors (use in because actors is a list)
if user_option == "4":
	movie_actor = input("Please enter the actor you are looking for ")
	for movie in movies: 
		title = movie["title"]
		actors = movie["actors"]
		if movie_actor in actors:
			print(f'{title}.')
