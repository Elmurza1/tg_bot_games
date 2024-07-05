class Person:
    def __init__(self, name_pm, age_pm):
        self.name = name_pm
        self.age = age_pm


class Teacher(Person):
    def __init__(self, subject_pm, name_pm, age_pm):
        self.subject = subject_pm
        self.name = name_pm
        self.age = age_pm

    def info(self):
        print(f'предмет {self.subject}, имя {self.name}, возраст {self.age}')

teacher = Teacher('math', 'stiv', 33)

teacher.info()