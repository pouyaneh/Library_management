from BasicValues import books
from book import Book

def addbook():
    _len = len(books)
    _id = books[_len - 1].id
    _title = input('enter title book : ')
    _author = input('enter author book : ')
    _id = int(_id[1:]) + 1
    _id = "B" + str(_id)
    books.append(Book(_id, _title, _author))
    input('     continue?')

def deletebook():
    j = 1
    for i in books:
        print(f'{j}.{i.title}')
        j += 1
    _delete = int(input('''
    0.cancel
    select number of title book : '''))
    books[_delete - 1].book_status()
    if _delete != 0 and books[_delete - 1].open[0] == 1 and books[_delete - 1].open[1] == 0:
        books.pop(_delete - 1)
    input('     continue?')

def bookediting():
    j = 1
    for i in books:
        print(f'{j}.{i.title}')
        j += 1
    _title = input("enter title book : ")
    j = 0 
    for i in books:
        if _title == i.title:
            break
        j += 1
    if j != len(books):
        _title = input("enter new title : ")
        _author = input("enter new author : ")
        books[j].title = _title 
        books[j].author = _author
    input('     continue?')
    

def booksinformation():
    j = 1
    for i in books:
        print(f'{j}. {i.id} = {i.title}')
        j += 1
    input('     continue?')
