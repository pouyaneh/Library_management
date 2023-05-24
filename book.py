class Book:
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author
        self.late_fee = 10000  # daily late fee in rials
        self.user_id = 0
        self.return_date = 0
        self.reservations = []
        self.open = [0, 0]
        #book status
    def book_status(self):
        if not self.reservations:
            self.open[0] = 0
        else: 
            self.open[0] = 1
    
    #receiving books
    def borrow(self, _user_id, _return_date):
        print(f"""  
        Book {self.title} ({self.id}) 
        is borrowed by user {_user_id} 
        until {_return_date}""")
        self.open[1] = 1
        self.return_date = _return_date
        self.user_id = _user_id
    #booking books
    def reserve(self, user_id):
        self.reservations.append(user_id)
        print('     Your name was included in the reservation list.')
    #The main function of receiving and booking books
    def borrowing(self, user_id, return_date = 0):
        self.book_status()
        if self.open[1] == 0:
            self.borrow(user_id, return_date)
            if self.open[0] == 1:
                self.reservations.pop(0)
        else:
            self.reserve(user_id)


    #delete borrower
    def borrower_update(self):
        self.user_id = 0
        self.return_date = 0
        self.open[1] = 0

    def calculate_delay_pentalty(self, _return_date):
        day = int(self.return_date)
        day = int((day % 100) +(((day % 10000) - (day % 100)) / 100) * 30 + (((day - (day % 10000)) / 10000) * 365))
        _day = int(_return_date)
        _day = int((_day % 100) +(((_day % 10000) - (_day % 100)) / 100) * 30 + (((_day - (_day % 10000)) / 10000) * 365))
        print(f'''
            The penalty for the delay 
            in returning the borrowed 
            book is {(_day % day) * self.late_fee} rial
            ''')
    #Penalty for delay in returning the borrowed book
    def delay_penalty(self, _return_date):
        if _return_date <= self.return_date:
            print('''
            Thank you !!
            for returning 
            the borrowed 
            book on time
            ''')
        else:
            self.calculate_delay_pentalty(_return_date)
    #The main function of returning books
    def returning(self, _user_id, _return_date):
        self.book_status()
        if self.open[0] == 1:
            print('''
            Error !!
            This book has not 
            been borrowed yet
            ''')
        else:
            if self.user_id == _user_id:
                self.delay_penalty(_return_date)
                self.borrower_update()
            else:
                print('''
            Error !!
            This book has not 
            been borrowed by you
                ''')
                