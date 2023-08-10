from faker import Faker


def name_faker():
    faker = Faker("ru-RU")
    name = faker.name()
    phone_number = faker.phone_number()
    print(f"Hello {name}, your phone number {phone_number}.")


def main():
    name_faker()