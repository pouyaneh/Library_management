from user import User
from book import Book
from BasicValues import books, users

def find_user(_id):
    _index = 0
    for index in users:
        if index.id == _id:
            break
        _index += 1
    return _index

def print_books():
    j = 1
    for i in books:
        print(f'{j}.{i.title}')
        j += 1
def print_user_book(_index):
    j = 1
    for i in users[_index].borrowed_books:
        for k in books:
            if k.id == i:
                print(f'{j}. {k.title} : {k.return_date} : {i}')
                break
        j += 1

def editing_information(_id):
    _index = find_user(_id)
    _choose = int(input(f'''
    0.back
    1.name : {users[_index].name}
    2.password : {users[_index].password}
    3.phone : {users[_index].phone}
    => '''))
    match _choose:
        case 1:
            users[_index].name = input('enter new name : ')
        case 2:
            users[_index].password = input('enter new password : ')
        case 3:
            users[_index].phone = input('enter new phone : ')

def borrowing_books(_id):
    _index = find_user(_id)
    print_books()
    __index = int(input('''0.cancel
    select number of title book : '''))
    if books[__index -1].user_id != _id and __index != 0 :
        books[__index - 1].book_status()
        if books[__index - 1].open[1] == 0 and books[__index - 1].open[0] == 0:
            _return_date = int(input('''
    The book is free to borrow.
    Enter the time of return of the book
    For example, March 24, 2022 = 20220324
        => '''))
            books[__index -1].borrowing(_id, _return_date)
            users[_index].borrow_book(books[__index - 1].id)
        elif books[__index - 1].open[1] == 0 and books[__index - 1].open[0] == 1 and books[__index - 1].reservations[0] == _id:
            _return_date = int(input('''
    The book is free to borrow just for you.
    Enter the time of return of the book
    For example, March 24, 2022 = 20220324
        => '''))
            books[__index -1].borrowing(_id, _return_date)
            users[_index].borrow_book(books[__index - 1].id)
        else:
            _return_date = int(input(f'''
    This book was borrowed by {books[__index - 1].user_id} 
    until the {books[__index - 1].return_date}
    Do you want to go on the reservation list?
    0.cancel
    1.yes
    =>'''))
            if(_return_date != 0):
                books[__index -1].borrowing(_id)
    input('     continue?')

def returning_book(_id):
    _index = find_user(_id)
    print_user_book(_index)
    _book_id = int(input('Enter the number of the book you want to return : '))
    _return_time = int(input('Enter the time of the book you want to return : '))
    _book_id = users[_index].borrowed_books.pop(_book_id - 1)
    for i in books:
        if i.id == _book_id:
            i.returning(_id, _return_time)
            break
    input('     continue?')
    
def extension_deadline(_id):
    _index = find_user(_id)
    print_user_book(_index)
    _book_id = input('Enter the ID of the book you want to extend the deadline : ')
    for i in books:
        if i.id == _book_id:
            if i.open[0] == 0:
                i.return_date = int(input('Enter the new deadline : '))
            else:
                print('It is not possible to extend the deadline')
            break
    input('     continue?')

def borrowed_books(_id):
    _index = find_user(_id)
    print_user_book(_index)
    input('     continue?')