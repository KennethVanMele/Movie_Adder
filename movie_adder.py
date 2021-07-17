from imdb import IMDb
from xlwt import Workbook

ia = IMDb()
f = open("movies.txt", "r")
i = 0
wb = Workbook()
s1 = wb.add_sheet('Sheet 1')

for line in f:
    movies = ia.search_movie(line)
    # bump movie up if not right one
    movie = ia.get_movie(movies[0].movieID)

    s1.write(i, 0, movie.get('title'))
    s1.write(i, 1, movie.get('rating'))
    s1.write(i, 2, movie.get('year'))

    genres = movie.get('genres')
    l_genres = ""
    for g in genres:
        if l_genres != "":
            l_genres = l_genres + ", " + g
        else:
            l_genres = g
    s1.write(i, 3, l_genres)

    plot = movie.get('plot')[0]
    plot = plot[:plot.rfind("::")]
    s1.write(i, 4, plot)
    i += 1
    print(movie.get('title') + ' added')

wb.save("movies.xls")
