# Procedural style (before OOP conversion)
def create_person(name, age):
    return {"name": name, "age": age}

def greet(person):
    print(f"Hello, {person['name']}!")

def have_birthday(person):
    person["age"] += 1
    print(f"Happy birthday! You're now {person['age']}")

john = create_person("John", 30)
greet(john)
have_birthday(john)