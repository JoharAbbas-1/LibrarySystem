class Librarians:
    payincrement = 1.03
    def __init__(self, first_name, last_name, pay, years_worked):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.years_worked = years_worked

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def increase_pay(self):
        self.pay =  int(self.pay * Librarians.payincrement) 

    def work_anniversary(self):
        self.years_worked = self.years_worked + 1
        self.increase_pay()

    def __repr__(self):
        return "Librarians('{}' '{}' '{}')".format(self.first_name, self.last_name, self.pay)
    
    
    @classmethod
    def set_raise_amount(cls, amount):
        cls.payincrement = amount
    
    @classmethod
    def librarians_string(cls, str_librarian):
        first_name, last_name, pay, years_worked = str_librarian.split('-')
        return cls(first_name, last_name, pay, years_worked)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 6 or day.weekday() == 5:
            return False 
        return True    
class Book:
    
    def __init__(self, name, publisher, genre, year):
        self.name = name
        self.publisher = publisher
        self.genre = genre
        self.year = year
        self.is_borrowed = False
    
    def mark_borrow(self):
        self.is_borrowed = True

    def book_availability(self):
        if self.is_borrowed == True: 
            return 'This book is not avaliable to be borrowed'
        return 'This book is avaliable to be borrowed'
    
    def mark_return(self):
        self.is_borrowed = False

       
    def BookandPublisher(self): 
        return '{} was published by {}'.format(self.name, self.publisher)   
    
    def __repr__(self):
        return "Book('{}')".format(self.name)

class Members:
    borrow_limit = 0
    borrow_time_period_limit = 0
    def __init__(self, member_first_name, member_last_name, member_status):
        self.member_first_name = member_first_name
        self.member_last_name = member_last_name
        self.member_status = member_status
        self.num_borrowed = 0
        self.borrow_period = 0

        
    def borrow_book(self, books):
        if self.num_borrowed >= self.borrow_limit:
            return ('You have either reached your limit of borrowing books or your status has not been confirmed yet, please contact support')
        elif  self.borrow_period >= self.borrow_time_period_limit:
            return "You have books pending to return"
        else:
            if books.is_borrowed == True:
                return'This book is not avaliable to be borrowed'
            else:
                self.num_borrowed = self.num_borrowed + 1
                books.mark_borrow()
                return 'You have successfully borrowed another book'

    def returning_book(self, rbooks):
        if rbooks.is_borrowed == True:
            rbooks.mark_return()
            self.num_borrowed = self.num_borrowed - 1
            return 'Thanks for returning the book'
        return 'This book has not been borrowed yet'

    def __str__(self):
        return '{}'.format(self.member_full_name) 
    
   
    @property
    def member_email(self):
        return '{}.{}@uni.members.co.uk'.format(self.member_first_name, self.member_last_name) 
    
    @property
    def member_full_name(self):
        return '{} {}'.format(self.member_first_name, self.member_last_name)

class Staff(Members):
    borrow_limit = 5
    borrow_time_period_limit = 8
    def __init__(self, member_first_name, member_last_name, member_status, member_faculty): 
        super().__init__(member_first_name, member_last_name, member_status)
        self.member_faculty = member_faculty
       
    
class Students(Members):
    borrow_limit = 3
    borrow_time_period_limit = 4    
    def __init__(self, member_first_name, member_last_name, member_status, member_course):
        super().__init__(member_first_name, member_last_name, member_status)
        self.member_course = member_course
   
class Library:
    def __init__(self):
        self.book = []
        self.member = []

    def add_member(self, members):
        self.member.append(members)

    def add_book(self, books):
        self.book.append(books)
    
    def find_book(self, name):
        for book in self.book:
            if book.name == name:
                return book
        return 'Book not found'
    
    def find_member(self, name):
        for member in self.member:
            if member.member_full_name == name:
                return member
        return 'Member not found'
    
    def borrowed(self, member_name, book_name):
        member = self.find_member(member_name)
        book = self.find_book(book_name)
        return member.borrow_book(book)


member_1 = Members('Joney', 'Jones', 'Student')
member_2 = Members('Tipsy', 'Hames', 'Teacher')

member_3 = Students('Timmy', 'Cook', 'Student', 'Computer Science')
member_4 = Staff('Josh', 'Atikson', 'Teacher', 'Science & Technology')

#member_2.member_first_name = 'Joe'

#print(member_3.member_email)
#print(member_3.borrow_book())
#print(member_3.borrow_book())
#print(member_3.borrow_book())
#print(member_3.borrow_book())
#print(member_3.member_course)
#print(member_4.member_faculty)
#print(member_2.member_email)
#print(member_3.num_borrowed)
librarian1= Librarians('Hoose', 'Loco', 2400, 3)
librarian2= Librarians('Niel', 'Congo', 2250, 2)


#print(librarian1)
#print(member_4)  
str_librarian_1 = "Rayan-Bhatti-500-15"

new_librarian_1 = Librarians.librarians_string(str_librarian_1)
#print(librarian1.fullname())
#print(librarian1.years_worked)
#print(librarian1.pay)
#print(new_librarian_1.fullname())

import datetime
my_day = datetime.date(2026, 6, 28)

#print(Librarians.is_workday(my_day))

#librarian1.work_anniversary()
#print(librarian1.years_worked)
#print(librarian1.pay)

#librarian1.set_raise_amount(1.02)

#librarian1.increase_pay()
#print(librarian1.pay)

book1 = Book('Great Wall of Johar', 'Johar Abbas', 'History', "2026")
book2 = Book('Great Wall of GOJO', 'Saturo Gojo', 'History', "2026")
book3 = Book('JJK', 'Hantei', 'Dark', '2025' )
book4 = Book('Vinland Saga', 'Saad', 'Drama', '2024')

library1 = Library()
library1.add_book(book1)
library1.add_book(book2)
library1.add_book(book3)
library1.add_book(book4)
library1.add_member(member_1)
library1.add_member(member_2)
library1.add_member(member_3)
library1.add_member(member_4)
findbook = library1.find_book('JJK')
findmember = library1.find_member('Timmy Cook')
#print(findbook)
#print(findmember)
#print(member_3.member_full_name)
result1 = library1.borrowed('Timmy Cook', 'JJK')
result2 = library1.borrowed('Timmy Cook', 'Great Wall of Johar')
result3 = library1.borrowed('Timmy Cook', 'Great Wall of GOJO')
result4 = library1.borrowed('Timmy Cook', 'Vinland Saga')
print(result1)
print(result2)
print(result3)
print(result4)
#print(library1.book)
#print(library1.member)

#for book in library1.book:
    #print(book.name)

#print(member_3.borrow_book(book1))
#print(member_3.borrow_book(book2))
#print(member_3.borrow_book(book3))
#print(member_3.borrow_book(book4))
#member_3.returning_book(book2)
#print(member_3.borrow_book(book4))
#print(book2.book_availability())
#print(book1.book_availability())
#book1.mark_borrow()
#print(book1.book_availability())
#book1.mark_return()
#print(book1.book_availability())
#print(book1.year)
#print(book2.name)
#print(book1.genre)
#print(book1.publisher)
#print(book1.BookandPublisher())