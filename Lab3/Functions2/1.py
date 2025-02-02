def score(x):
    return x["imdb"] > 5.5

def high(x):
    return [i for i in x if i["imdb"] > 5.5]

def category(x, ctgr):
    return [i for i in x if i["category"] == ctgr]

def average_imdb(x):
    return sum(i["imdb"] for i in x) / len(x) if x else 0

def average_imdb_by_category(x, y):
    category_movies = category(x, y)
    return average_imdb(category_movies)






movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

print(score(movies[0]))
print(high(movies))
print(category(movies, "Romance"))
print(average_imdb(movies))
print(average_imdb_by_category(movies, "Romance"))