class Employee:
    def __init__(self, my_name_pm, stazh_pm):
        self.stazh = stazh_pm
        self.name = my_name_pm

class Worker(Employee):
    def profile(self,):
        print(f'меня зовут {self.name}, мой стаж работы {self.stazh}')




class Manager(Employee):
    def ffire(self, worker):
        print(f'сотрудник,{worker.name}уволен,  менджером,{self.name}')





nurs = Worker(my_name_pm='нурсултан', stazh_pm=5)
asan = Worker(my_name_pm= 'асан', stazh_pm=10)

kanat = Manager(my_name_pm='канат', stazh_pm=15)

asan.profile()
nurs.profile()

kanat.ffire(nurs)

