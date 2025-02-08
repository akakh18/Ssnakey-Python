class Person:
    # Constructor
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    def get_person_name(self) -> str:
        return self.name

    def get_person_age(self) -> int:
        return self.age

    def set_person_name(self, name: str) -> any:
        return Person(name, self.age)

    def set_person_age(self, age: int) -> any:
        return Person(self.name, age)


def increase_person_age_by(person: Person, age: int) -> None:
    person.set_person_age(person.get_person_age() + age)


if __name__ == "__main__":
    person_john = Person("John", 18)
    person_avto = Person("Avto", 25)
    print("John:")
    print("Name:", person_john.get_person_name())
    print("Age:", person_john.get_person_age())
    print("Avto:")
    print("Name:", person_avto.get_person_name())
    print("Age:", person_avto.get_person_age())


    increase_person_age_by(person_avto, 1)
    print("Avto now:")
    print("Name:", person_avto.get_person_name())
    print("Age:", person_avto.get_person_age())

    person_avto = person_avto.set_person_age(person_avto.get_person_age() + 1)
    print("Avto now:")
    print("Name:", person_avto.get_person_name())
    print("Age:", person_avto.get_person_age())
