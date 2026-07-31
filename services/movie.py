from django.db.models import QuerySet

from db.models import Movie, Genre, Actor

def get_movies(
        genres_ids: list = None,
        actors_ids: list = None
) -> QuerySet[Movie, Movie]:
    return Movie.objects.filter(
        genres__in=genres_ids,
        actors__in=actors_ids
    )


def get_movie_by_id(
        movie_id: int
) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list = None,
        actors_ids: list = None,
) -> None:
    if genres_ids is None:
        genres_ids = []
    if actors_ids is None:
        actors_ids = []

    movie = Movie.objects.create()
    movie.title = movie_title
    movie.description = movie_description
    movie.genres.set(genres_ids)
    movie.actors.set(actors_ids)
    movie.save()
