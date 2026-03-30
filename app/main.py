class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list) -> list:

    Person.people.clear()
    new_list = {person["name"]: Person(person["name"],
                                       person["age"]) for person in people}
    for person in people:
        if person.get("wife"):
            new_list[person["name"]].wife = new_list[person["wife"]]
        if person.get("husband"):
            new_list[person["name"]].husband = new_list[person["husband"]]
    return list(new_list.values())
