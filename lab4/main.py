"""Лабораторна 4 — точка входу."""
from datetime import date

from f_requests import build_url
from f_numpy import matrix_stats
from f_pandas import make_table
from f_colorama import colored
from f_tqdm import progress
from f_rich import show_table
from f_dateutil import age_in_years
from f_pyfiglet import banner
from f_emoji import to_emoji
from f_faker import fake_person
from f_os import list_py_files
from f_json import save_json
from f_random import pick_random
from f_math import circle_area
from f_hashlib import sha256_of


def main():
    print(banner("Lab 4"))
    print(to_emoji("Готово :thumbs_up: :snake:"))
    print(colored("URL:", "CYAN"), build_url("https://example.com/api", {"q": "python", "page": 2}))
    print("numpy (слід, det):", matrix_stats(3))
    df, avg = make_table(["Оля", "Іван", "Марія"], [90, 75, 88])
    print(df)
    print("Середній бал:", avg)
    progress(30)
    show_table(list(zip(df["name"], df["score"])))
    print("Вік:", age_in_years(date(2005, 5, 17)), "років")
    name, addr = fake_person()
    print("Faker:", name, "|", addr)
    print("Файли:", list_py_files())
    print("Випадкове:", pick_random(["a", "b", "c"]))
    print("Площа кола r=5:", circle_area(5))
    print("SHA-256:", sha256_of("lab4"))
    print("Збережено:", save_json({"name": name, "average": avg}))


if __name__ == "__main__":
    main()
