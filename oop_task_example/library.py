class Library:
    def __init__(self, title_pm, author_pm):
        self.title = title_pm
        self.author = author_pm
        self.book = []




    def add_book(self, new_book):
        self.book.append(new_book)

    def list_books(self):
        return self.book

    def remove_book(self, rem_book):
        self.book.remove(rem_book)

    def find_book_by_title(self, book_title: str):
        for item in self.book:
            if item.title == book_title:
                return item

    def find_book_by_author(self, author_name: str):
        for item in self.book:
            if item.author == author_name:
                return item


book1 = Library('бойцовский клуб', 'чак паланик')

book2 = Library('самый богатый человек в вавилоне', 'джон клейсон')



book2.add_book('cat')
print(book2.list_books())

book1.add_book('dog')

print(book1.list_books())

book1.add_book('fff')
print(book1.list_books())

