import json



save_data = {
    "movie" : "inception" ,
    "date" : "2010" ,
    "actor" : ["Leonardo" , "page"]
}


with open("MOVIE.json" , "w") as file:
    json.dump(save_data, file)


with open("MOVIE.json" ,"r") as file:
    movie = json.load(file)

print(f"Movie : {movie["actor"]}")