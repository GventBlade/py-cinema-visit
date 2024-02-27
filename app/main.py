from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: str, hall_number: int,
                 cleaner: str, movie: str) -> None:
    cb = CinemaBar()
    ch = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)

    for customer_data in customers:
        customer = Customer(customer_data["name"], customer_data["food"])
        cb.sell_product(customer, customer.food)

    ch.movie_session(movie, [Customer(c["name"], c["food"])
                             for c in customers], cleaner_instance)
