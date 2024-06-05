class Book:
    def __init__(self, name_pm, name_autor_pm, page_pm):
        self.name = name_pm
        self.page = page_pm
        self.avtor = name_autor_pm
    def info_mini(self):
        info = f"название,{self.name} автор,{self.avtor} кол-во страниц,{self.page}"
        return info


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, rem_book: Book):
        self.books.remove(rem_book)

    def list_book(self):
        return self.books

    def find_book_by_tytle(self, book):
        for item in self.books:
            if item.name == book:
                return item

    def find_book_by_autor(self, book):
        for item in self.books:
            if item.avtor == book:
                return item




lib = Library()


new_book = Book(name_pm='бойцовский клуб', name_autor_pm='чак паланик', page_pm=283)

book2 = Book(name_pm='самый богатый человек в вавилоне',  name_autor_pm='джордж клейсон', page_pm=185)

print(new_book.info_mini())


print(book2.info_mini())

lib.add_book(new_book)
print(lib)

print(lib.find_book_by_tytle())