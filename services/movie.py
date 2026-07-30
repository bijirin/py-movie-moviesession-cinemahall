from django.db.models import QuerySet

from db.models import Movie, Genre, Actor

def get_movies(
        genre_ids: list,
        actors_ids: list
) -> QuerySet[Movie, Movie]:
    return Movie.objects.filter(
        genres__in=genre_ids,
        actors__in=actors_ids
    )


def get_movie_by_id(
        movie_id: int
) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genre_ids: list = None,
        actors_ids: list = None,
) -> None:
    if genre_ids is None:
        genre_ids = []
    if actors_ids is None:
        actors_ids = []

    movie = Movie()
    movie.title = movie_title
    movie.description = movie_description
    movie.genres = Genre.objects.filter(id__in=genre_ids)
    movie.actors = Actor.objects.filter(id__in=actors_ids)
    movie.save()
