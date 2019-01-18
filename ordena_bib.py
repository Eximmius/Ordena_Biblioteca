# Ordenação de Livros
# 18/01/2019

import operator

class Book:
  def __init__(self,title,author,year):
    self.title=title
    self.author=author
    self.year=year

  def __repr__(self):
    return f'{self.title} -- {self.author} -- {self.year}'

  @classmethod
  def from_csv(cls,str):
    pass
        #split
        #return cls(title,author, year)

class Library:  
  def __init__(self,books=None):
    self.n_of_books=0
    if books is None:
      self.books=[]      
    else:
      self.books = books
      self.n_of_books=len(books)
      
  def add_book(self,book):
    if book not in self.books:
      self.books.append(book)
      self.n_of_books += 1

  def remove_book(self):
    pass
      
  def __repr__(self):
    libr_str = 'Lib has '+f'{self.n_of_books} '+'books\n'
    for book in self.books:
      libr_str += book.title +' -- '+ book.author +' -- '+ str(book.year)+'\n'
    return libr_str

  def sort_Lib(self,attr=None,rev=None):
      "order..."
      # Lib -> cls Library with list of books
      # attr -> Ordered List of preferential attributes
      # rev -> List if reverse=True/False for attr

      if attr is None:
        return
      attr.reverse()
      rev.reverse()
      i=0
      for attribute in attr:
          self.books.sort(key = operator.attrgetter(attribute),reverse=rev[i])
          i+=1

      return



b1 = Book('A','C',4)
b2 = Book('B','A',2)
b3 = Book('C','D',5)
b4 = Book('D','A',1)
b5 = Book('D','C',3)
b6 = Book('B','B',2)
b7 = Book('B','B',1)
b8 = Book('C','C',1)

books = [b1,b2,b3,b4,b5,b6,b7,b8]
Lib = Library(books)
print(Lib)

attr=['title','author']
rev=[False,False]
Lib.sort_Lib(attr,rev)
print('Sorted Lib\n')
print(Lib)





