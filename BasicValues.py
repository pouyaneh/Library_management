from book import Book
from admin import Admin
from user import User

books = [Book("B74001", "Structure and Interpretation of Computer Programs", "Harold Abelson"),
         Book("B74002", "Clean Code", "Robert C. Martin"),
         Book("B74003", "Introduction to Algorithms", "Thomas H. Cormen"),
         Book("B74004", "Code Complete", "Steve McConnell"),
         Book("B74005", "Design Patterns", "Erich Gamma"),
         Book("B74006", "The Pragmatic Programmer", "Andrew Hunt"),
         Book("B74007", "Head First Design Patterns", "Eric Freeman"),
         Book("B74008", "Refactoring", "Martin Fowler"),
         Book("B74009", "The Art of Computer Programming", "Donald E. Knuth"),
         Book("B74010", "The Clean Coder", "Robert C. Martin")
         ]
users = [User(2222222222, "NOBODY", "1", "USER_TEST"),
         User(2857423862, "ali akbari", "123", "09123456789"),
         User(2857423872, "Haleh Afshar", "456", "09010000000"),
         User(2857423882, "Touraj Atabaki", "789", "09202020202")
         ]
admins = [Admin(1111111111, "NOONE", "1", "ADMIN", "TEST"),
          Admin(1564867231, "Tim Lee", "123", "PhD in Computer Science", "Computer scientist"),
          Admin(1564867241, "Alan Turing", "456", "PhD in Computer Science", "Mathematician"),
          Admin(1564867251, "James Gosling", "789", "PhD in Computer Science", "Data Analysis")
          ]

books[3].borrowing(2222222222, 20230420)
books[4].borrowing(2222222222, 20230420)
books[5].borrowing(2222222222, 20230420)
books[6].borrowing(2222222222, 20230420)
books[7].borrowing(2222222222, 20230420)
users[0].borrow_book(books[3].id)
users[0].borrow_book(books[4].id)
users[0].borrow_book(books[5].id)
users[0].borrow_book(books[6].id)
users[0].borrow_book(books[7].id)
books[4].borrowing(2857423872)
books[5].borrowing(2857423872)
books[6].borrowing(2857423872)
books[7].borrowing(2857423872)
books[5].borrowing(2857423862)
books[6].borrowing(2857423862)
books[7].borrowing(2857423862)
