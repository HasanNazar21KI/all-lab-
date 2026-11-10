from faker import Faker


def fake_person():
    """faker: генерує фейкові дані людини."""
    f = Faker("uk_UA")
    return f.name(), f.address().replace("\n", ", ")
