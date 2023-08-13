import random
import string

def random_name(length: int = 8) -> str:
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def random_phone():
    return random.randint(1000000000, 9999999999)

class Person():
    name: str
    phone: int
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    
    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}"
   

person = Person('bob', 128467122)
print(person)