from django.db.models import QuerySet

from db.models import CinemaHall


def get_cinema_halls() -> QuerySet[CinemaHall, CinemaHall]:
    return CinemaHall.objects.all()


def create_cinema_hall(
        hall_name: str,
        hall_rows: int,
        hall_seats_in_row: int
) -> None:
    cinema_hall = CinemaHall()
    cinema_hall.name = hall_name
    cinema_hall.rows = hall_rows
    cinema_hall.seats_in_row = hall_seats_in_row
    cinema_hall.save()
