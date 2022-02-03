import pandas as pd


ratings_movies = pd.read_csv('data/movies_data/ratings_movies.csv')

# напишем функцию выделить из признака title год выпуска фильма
# библиотека для регулярных выражений
import re 
def get_year_release(arg):
    #находим все слова по шаблону "(DDDD)"
    candidates = re.findall(r'\(\d{4}\)', arg) 
    # проверяем число вхождений
    if len(candidates) > 0:
        #если число вхождений больше 0,
	#очищаем строку от знаков "(" и ")"
        year = candidates[0].replace('(', '')
        year = year.replace(')', '')
        return int(year)
    else:
        #если год не указан, возвращаем None
        return None
    
    
# Создайте в таблице новый признак year_release, который соответствует году выпуска фильма.
# У скольких фильмов не указан год их выпуска?
ratings_movies['year_release'] = ratings_movies['title'].apply(get_year_release)
print(ratings_movies.info())


# Какой фильм title, выпущенный в 1999 году, получил наименьшую среднюю оценку зрителей?
mask = ratings_movies['year_release'] == 1999
print(ratings_movies[mask].groupby('title')['rating'].mean().sort_values())


# Какое сочетание жанров фильмов genres, выпущенных в 2010 году, получило наименьшую среднюю оценку?
mask = ratings_movies['year_release'] == 2010
print(ratings_movies[mask].groupby('genres')['rating'].mean().sort_values())


# Найдите идентификатор пользователя userId, который посмотрел больше всего фильмов с сочетаниями разных жанров genres.
print(ratings_movies.groupby('userId')['genres'].nunique().sort_values(ascending=False))


# Найдите пользователя userId, который выставил наименьшее количество оценок rating, но его средняя оценка фильмам mean наибольшая.
# Чтобы рассчитать несколько параметров для каждого пользователя (количество оценок и среднюю оценку), можно воспользоваться методом agg() на сгруппированных данных.
print(ratings_movies.groupby('userId')['rating'].agg(
    ['count', 'mean']
).sort_values(['count', 'mean'], ascending=[True, False]))


# Найдите сочетание жанров фильма genres, выпущенного в 2018 году, 
# который имеет наибольший средний mean рейтинг rating, 
# и при этом число выставленных ему оценок больше 10.
mask = ratings_movies['year_release'] == 2018
grouped = ratings_movies[mask].groupby('genres')['rating'].agg(
    ['mean', 'count']
)
grouped[grouped['count']>10].sort_values(
    by=['mean', 'count'],
    ascending=[False, False]
)

# Добавьте в таблицу новый признак year_rating — год выставления оценки. 
# Создайте сводную таблицу, которая иллюстрирует зависимость среднего рейтинга фильма от года выставления оценки и жанра. 
ratings_movies['date'] = pd.to_datetime(ratings_movies['date'])
ratings_movies['year_rating'] = ratings_movies['date'].dt.year
pivot = ratings_movies.pivot_table(
    index='genres',
    columns='year_rating',
    values='rating',
    aggfunc='mean'
)
print(pivot)


# Какое сочетание жанров фильмов genres, выпущенных в 2018 году, получивших наивысшую среднюю оценку?
mask = ratings_movies['year_release'] == 2018
print(ratings_movies[mask].groupby('genres')['rating'].mean().sort_values())



# тенденция рейтинга с 1996 по 2018 для жанра Comedy
mask = ratings_movies['genres'] == 'Comedy'
mask_year = ratings_movies['year_rating'] > 1996
grouped = ratings_movies[mask][mask_year].groupby('year_release')['rating'].mean()
print(grouped.sort_values())