import random
import string
from person import Person
from sorting import bubble_sort


def random_name(length: int = 8) -> str:
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def random_phone():
    return random.randint(1000000000, 9999999999)

phone_book = [None] * 50

for i in range(50):
    phone_book[i] = Person(random_name(), random_phone())

bubble_sort(phone_book, 'phone')
for contact in phone_book:
    print(contact)
