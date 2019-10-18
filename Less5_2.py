"""
2) Employee (наследуемся от Person) (добавляются свойства: должность, опыт работы, зарплата)
** (только для продвинутых) Можете в конструкторе проверить, что в опыт работы и зарплата не отрицательные 😊
Реализовать новые методы:
1.	возвращает должность с приставкой, которая зависит от опыта работы: Junior — менее 3 лет, Middle — от 3 до 6 лет, Senior — больше 6 лет.
Т.е. метод должен вернуть позицию с приставкой Junior/Middle/Senior <position>. Если, например у вас объект имел должность “programmer” с опытом 2 года, метод должен вернуть “Junior programmer”
2.	метод, который увеличивает зарплату на сумму, которую вы передаёте аргументом.
"""
from Less5_1 import Person


class Employee(Person):
    def __init__(self, full_name='', year_of_birth=None, position=None, experience=0, salary=0, bonus=0):
        Person.__init__(self, full_name, year_of_birth)

        self.position = position
        self.experience = experience
        self.salary = salary + bonus
        self.bonus = bonus

    def status(self):
        if self.experience < 3:
            return self.position + " Junior"
        elif 3 <= self.experience > 6:
            return self.position + " Middle"
        else:
            return self.position + " Senior"


    # def __str__(self):
    #     return "<Employee object: {}. Age is {}. Position {}. Salary {}>".format(self.full_name(),
    #                                                                                 self.only_surname(), self.age(),
    #                                                                               self.status(), self.salary())
    #


if __name__ == "__main__":
    p1 = Employee('Peter Pen', 2000, 'QA Automation', 5, 3000, 500)
    print(p1.full_name)
    print(p1.age())
    print(p1.status())
    print(p1.experience)
    print(p1.salary)
    # print(p)



