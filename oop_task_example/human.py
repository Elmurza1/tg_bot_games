
'''
class Human:
    def __init__(self, name_pm, age_pm, fee_pm):
        self.name = name_pm
        self.age = age_pm
        self.__fee = fee_pm

    def inf(self):
        info_human = f'имя,{self.name}  возраст,{self.__age}  язык,{self.language}'
        return info_human


my_maclovin = Human(name_pm='бектур', age_pm= 43, language_pm='кыргызский' )

print(my_maclovin.inf())

print(my_maclovin.language)


class Gogo(Human):
   pass 
'''


class Worker:
    def __init__(self, name_pm, age_pm, fee_pm):
        self.name = name_pm
        self.age = age_pm
        self.__fee = fee_pm

    def get_increase(self):
        return self.__fee

    def set_fee(self, fee: int):
        if fee > 0:
            self.__fee = fee


  #  def increase_fee(self):
   #     self.__fee +=100
   #     return self.__fee



my_worker = Worker(name_pm='sultan', age_pm=27, fee_pm=50000)

plata = my_worker.get_increase()


my_worker.set_fee(64_000)

print(my_worker.get_increase())


class Manager(Worker):
 pass








