import datetime as dt

from django.db.models import QuerySet

from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(
        movie_show_time: dt.datetime,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    movie_session = MovieSession()
    movie_session.show_time = movie_show_time
    movie_session.cinema_hall = (
        CinemaHall.objects.get(id=cinema_hall_id)
    )
    movie_session.movie = (
        Movie.objects.get(id=movie_id)
    )
    movie_session.save()


def get_movie_sessions(
        session_date: dt.datetime
) -> QuerySet[MovieSession, MovieSession]:
    return MovieSession.objects.filter(show_time=session_date)


def get_movie_session_by_id(
        movie_session_id: int
) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: dt.datetime,
        movie_id: int=0,
        cinema_hall_id: int=0
) -> None:
    movie_session = MovieSession.objects.get(id=session_id)
    movie_session.show_time = show_time
    movie_session.movie = Movie.objects.get(id=movie_id)
    movie_session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    movie_session.save()


def delete_movie_session_by_id(
        session_id: int
) -> None:
    movie_session = MovieSession.objects.get(id=session_id)
    movie_session.delete()

