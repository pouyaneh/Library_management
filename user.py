class User:
    def __init__(self, id, name, password, phone):
        if len(str(id)) != 10 or str(id)[9] != '2':
            raise ValueError("Invalid ID")
        self.id = id
        self.name = name
        self.password = password
        self.phone = phone
        self.borrowed_books = []

    def borrow_book(self, book_id):
        self.borrowed_books.append(book_id)
        print(f"""  
        User {self.id} has 
        borrowed book {book_id}""")
    
    def Book_delivery(self, book_id):
        i = 0
        for j in self.borrowed_books:
            if book_id == j:
                break
            i += 1
        self.borrowed_books.pop(i)