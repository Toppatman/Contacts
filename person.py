class Person():
    name: str
    phone: int
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    
    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}"
   