class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list) -> list:

    new_list = {}
    for person in people:
        new_person = Person(person["name"], person["age"])
        new_list[person["name"]] = new_person
    for person in people:
        if "wife" in person:
            new_list[person["name"]].wife = new_list[person["wife"]]
        if "husband" in person:
            new_list[person["name"]].husband = new_list[person["husband"]]
    return list(new_list.values())
