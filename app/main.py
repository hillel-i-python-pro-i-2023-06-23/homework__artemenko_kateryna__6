from app.services.generate_users import show_users
from app.services.get_requests import get_astronaut
from app.services.read_csv import read_csv_file
from app.services.read_file import read_file


def main():
    read_file()
    show_users()
    get_astronaut()
    read_csv_file()

