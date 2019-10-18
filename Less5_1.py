
class Person:

    import datetime
    now = str(datetime.datetime.now())[:4]

    def __init__(self, full_name='', year_of_birth=None):
        self.full_name = full_name
        self.year_of_birth = year_of_birth

    def only_name(self):
        return self.full_name.split()[0]

    def only_surname(self):
        return self.full_name.split()[1]

    def age(self, to_year=now):
        return int(to_year) - int(self.year_of_birth)

    def __str__(self):
        return "<Person object: {} {}. Age is {}>".format(self.only_name(), self.only_surname(), self.age())


if __name__ == "__main__":
    person1 = Person('Peter Pen', 2000)
    print(person1)

    print(person1.only_name())
    print(person1.only_surname())
    print(person1.age())




