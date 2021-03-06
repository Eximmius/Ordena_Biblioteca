# Ordenação de Livros
# Autor: Ian Schmiegelow Dannapel
# 19/01/2019

import operator
import csv


class Book:
    book_n = 0

    def __init__(self, title, author, year):
        Book.book_n += 1
        self.number = Book.book_n
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f'{self.number} -- {self.title} -- {self.author} -- {self.year}'


class Library:
    def __init__(self, books=None):
        self.n_of_books = 0
        if books is None:
            self.books = []
        else:
            self.books = books
            self.n_of_books = len(books)

    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
            self.n_of_books += 1

    def remove_book(self):
        return NotImplemented

    def __repr__(self):
        libr_str = 'Lib has '+f'{self.n_of_books} '+'books\n'
        for book in self.books:
            libr_str += str(book.number) + ' -- ' + book.title + \
                ' -- ' + book.author + ' -- ' + str(book.year)+'\n'
        return libr_str

    def sort_Lib(self, attr, rev):
        # Lib -> cls Library with list of books
        # attr -> Ordered List of preferential attributes
        # rev -> List if reverse=True/False for attr

        error_sort = True
        attr.reverse()
        rev.reverse()
        i = 0

        for attribute in attr:
            try:
                self.books.sort(key=operator.attrgetter(
                    attribute), reverse=rev[i])
                i += 1
                error_sort = False
            except Exception:
                error_sort = True
                break
        return error_sort


books = []
with open('books.csv', 'r') as csv_f:
    csv_reader = csv.DictReader(csv_f)
    for line in csv_reader:
        books.append(Book(line['TITLE'], line['AUTHOR'], line['YEAR']))
    Lib = Library(books)
    print('Livros Cadastrados')

attr = []
rev = []
error_config = False
with open('ordena_bib.config', 'r') as f:
    for line in f:
        if (line[0] == '1') or (line[0] == '2') or (line[0] == '3'):
            try:
                num, attribute, reverse = line.split(',')
                attr.append(attribute.strip())
                rev.append(reverse.strip() == 'desc')
                error_config = False
            except Exception:
                error_config = True
                break
    print('Configurações lidas')

error_sort = True
if not error_config:
    error_sort = Lib.sort_Lib(attr, rev)

with open('book_sorted.csv', 'w') as csv_f:
    csv_writer = csv.writer(csv_f, lineterminator='\n')
    csv_writer.writerow(['NUMBER', 'TITLE', 'AUTHOR', 'YEAR'])
    if not error_sort:
        for book in Lib.books:
            csv_writer.writerow(
                [book.number, book.title, book.author, book.year])
        print('Ordenação realizada com sucesso, verifique arquivo')
    elif error_config:
        print('Ordering Exception')
        csv_writer.writerow(['Ordering Exception'])
    else:
        print('Nenhuma ordenação realizada')
