from book import Book
from admin import Admin
from user import User
from validation import AdminValidation, UserValidation
from BasicValues import books, users, admins
from AdminOption import addbook, deletebook, bookediting, booksinformation
from UserOptions import editing_information, borrowed_books, extension_deadline, borrowing_books, returning_book

page = 0
___id = 0
while True != False:
    #frist page
    if page == 0:
        page = int(input('''
        1.User
        2.Admin
        7.save name books and user in file
        9.Exit
        '''))
    #user page
    if page == 1:
        page = int(input('''
        0.Back
        3.Log in
        4.Log up
        9.Exit
        '''))
    #admin log in
    if page == 2:
        _id = int(input('Enter ID : '))
        _password = input('Enter Password : ')
        page = AdminValidation(_id, _password)
        ___id = _id
    #user log in
    if page == 3:
        _id = int(input('Enter ID : '))
        _password = input('Enter Password : ')
        page = UserValidation(_id, _password)
        ___id = _id
    #user log up
    if page == 4:
        _id = users[len(users) - 2].id + 10
        _name = input('Enter Name : ')
        _password = input('Enter Password : ')
        _phone = input('Enter phone : ')
        users.append(User(_id ,_name, _password, _phone))
        ___id = _id
        page = 10
    #successful admin login
    if page == 5:
        _page = int(input(f'''
        id : {___id}

        1.Add book
        2.Book editing
        3.Delete the book
        4.Books information
        5.Log Out
        '''))
        match _page:
            case 1:
                addbook()
            case 3:
                deletebook()
            case 2:
                bookediting()
            case 4:
                booksinformation()
            case 5:
                page = 0
                _page = 0
                ___id = 0
            case _:
                break
    #successful user login
    if page == 6:
        _page = int(input(f'''
        id : {___id}

        1.Editing information
        2.Borrowing books
        3.returning book
        4.Extension of the book return deadline
        5.My borrowed books
        6.Log Out
        '''))
        match _page:
            case 1:
                editing_information(___id)
            case 5:
                borrowed_books(___id)
            case 4:
                extension_deadline(___id)
            case 2:
                borrowing_books(___id)
            case 3:
                returning_book(___id)
            case 6:
                page = 0
                _page = 0
                ___id = 0
            case _:
                break
    #fils
    if page == 7:
        file = open('books.txt', 'w')
        for i in books:
            file.writelines(f'{i.id} : {i.title} , {i.author}  \n')
        file.close()
        file = open('users.txt', 'w')
        for i in users:
            file.writelines(f'{i.id} : {i.name} , {i.phone}  \n')
        file.close()
        page = 0
    #Login failed
    if page == 8:
        print('''
        Invalid Values
        Login failed
        Please try again
        ''')
        page = 0
        ___id = 0
    if page == 9:
        exit()
    #Successful membership new user
    if page == 10:
        print(f'''
        Successful membership
        Remember your
        ID : {___id}
        and password 
        ''')
        page = 3
        ___id = 0