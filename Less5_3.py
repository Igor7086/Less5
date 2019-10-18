from Less5_2 import Employee


class ITEmployee(Employee):
    def __init__(self, *args, **kwargs):
        Employee.__init__(self, *args, **kwargs)
        self.skills = []

    def add_skill(self, new_skill):
        self.skills.append(new_skill)
        return self.skills

    # def __str__(self):
    #     return "<Employee object: {}. Age is {}. Position {}. Salary {}. Skills {}>".format(self.full_name(),
    #                                                                                         self.only_surname(),
    #                                                                                         self.age(), self.status(),
    #                                                                                         self.salary(),
    #                                                                                         self.add_skill)


if __name__ == "__main__":
    p1 = ITEmployee('Peter Pen', 2000, 'QA Automation', 5, 3000, 500)
    print(p1.add_skill(['Python', 'Selenium']))
    print(p1)






# class ITEmployee(Employee):
#     def __init__(self, full_name, year_of_birth, position, experience, salary, bonus, skills=None):
#         Employee.__init__(self, full_name, year_of_birth, position, experience, salary, bonus)
#
#         self.skills = skills
#
#     def add_skill(self, new_skill):
#         self.skills.append(new_skill)
#         return self.skills
#
#
# if __name__ == "__main__":
#     p1 = ITEmployee('Peter Pen', 2000, 'QA Automation', 5, 3000, 500, 'Python')
#     print(p1.add_skill)










