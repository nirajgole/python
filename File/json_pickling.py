import jsonpickle


class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


c = Cat("Garfield", "Tabby")

# with open('cats.json', 'w') as file:
#     frozen = jsonpickle.encode(c)
#     file.write(frozen)

with open("cats.json", "r") as file:
    contents = file.read()
    unfrozen = jsonpickle.decode(contents)
    print(unfrozen)
