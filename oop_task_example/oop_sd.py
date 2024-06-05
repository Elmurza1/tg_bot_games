class Person:
    def __init__(self, name_pm, age_pm):
        self.name = name_pm
        self.age = age_pm



    def ask_qustion(self, qustion: str):
        print(f'у меня вопрос: {qustion}')

    def answer(self, answer_text: str):
        print(f'ответ:{answer_text}')


class Student(Person):


    def say_hare(self):
        print(f'меня зовут {self.name} я здесь')




class Teacher(Person):


    def say(self):
        print('кто присутствует?')




nur = Student(name_pm='нуржигит', age_pm='20')
asan = Student(name_pm='асан', age_pm='30')

maria = Teacher(name_pm='мария', age_pm='40')


nur.say_hare()
