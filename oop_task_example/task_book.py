class Book:
    def __init__(self, name_pm, name_autor_pm, page_pm):
        self.name = name_pm
        self.page = page_pm
        self.avtor = name_autor_pm
    def info_mini(self):
        info = f"название,{self.name} автор,{self.avtor} кол-во страниц,{self.page}"
        return info

new_book = Book(name_pm='бойцовский клуб', name_autor_pm='чак паланик', page_pm=283)

book2 = Book(name_pm="самый богатый человек в вавилоне", name_autor_pm="роберт")

print(new_book.info_mini())
print(new_book.page)

