# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 04:15:34 2018

@author: zhangx
"""
from collections import namedtuple
class Author(object):
    def __init__(self, name, date_of_birth, nationality, age):
        self.date_of_birth = date_of_birth
        self.age = age
        self.name = name
        self.nationality = nationality
        self.authors = []
    def get_age(self):
        return self.age
    def __str__(self):
        return "The Author is:" + str(self.name)+ "; Nationality:" + str(self.nationality) + "; Age:" + str(self.age)
    def update_info(self, new_name, new_nationality, new_date_of_birth):
        self.name = new_name
        self.nationality = new_nationality
        self.date_of_birth = new_date_of_birth
    def load_file(self, filename):
        self.listname = []
        self.list = open(filename,'r')
        for line in self.list:
            self.listname.append(line.strip())
        return self.listname
    def add_author(self, author_name):
        #self.authors = []
        self.authors.append(author_name)
        #if A_name not in self.listname:
            #self.listname.append(A_name)
        #else:self.author.append(A_name)
    def del_author(self, author_name):
        if author_name in self.listname:
            self.listname.remove(author_name)
    def search_by_name(self, author_name):
        author_under_this_name = []
        for author in self.authors:
            if author.name == author_name:
                author_under_this_name.append(author)
        return author_under_this_name
    def search_by_natonality(self, nation):
        author_under_this_nation = []
        for author in self.authors:
            if author.nationality == nation:
                author_under_this_nation.append(author)
        return author_under_this_nation
    def search_by_agerange(self, agelow, agehigh):
        author_under_this_agerange = []
        for author in self.authors:
            if author.age >= agelow and author.age <= agehigh:
                author_under_this_agerange.append(author)
        return author_under_this_agerange

class Book(object):
    def __init__(self, name, author, publisher):
        #Author.__init__(self,author)  
        self.name = name
        self.publisher = publisher
        self.books = []
    def __str__(self):
        return "The Book is:" + str(self.name)+ "; Author:" + str(self.author) + "; Publisher:" + str(self.publisher)
    def update_info(self, new_name, new_author, new_publisher):
        self.name = new_name
        self.author = new_author
    def load_file(self, filename):
        self.listname = []
        self.list = open(filename,'r')
        for line in self.list:
            self.listname.append(line.strip())
        return self.listname
    def add_book(self, book_name):
        self.books.append(book_name)
    def del_book(self, book_name):
        if book_name in self.listname:
            self.listname.remove(book_name)
    def search_by_name(self, name):
        book_under_this_name = []
        for book in self.books:
            if book.name == name:
                book_under_this_name.append(book)
        return book_under_this_name
    def search_by_author_name(self, author_name):
        Author.search_by_name(author_name)
    def search_by_nationality(self, nationality):
        Author.search_by_natonality(nationality)
    def search_by_age(self, age):
        author_under_this_age = []
        for author in Author.authors:
            if author.age == age:
                author_under_this_age.append(author)
            return author_under_this_age

class User(object):
    def __init__(self, name, year_of_the_birth, address, phone):
        self.name = name
        self.year_of_the_birth = int(year_of_the_birth)
        self.address = address
        self.phone = phone
        self.users = []
    def __str__(self):
        address_split = self.address.split(', ')
        city = address_split[1]
        country = address_split[2]
        return "The User is: " + str(self.name)+ "; Age: " + str(2018-self.year_of_the_birth) + "; City: " + city + "; Country: " + country + "; Phone: " + str(self.phone)
    def update_info(self, new_name, new_address, new_phone):
        self.name = new_name
        self.address = new_address
        self.phone = new_phone
    def load_file(self, filename):
        self.listname = []
        self.list = open(filename,'r')
        for line in self.list:
            self.listname.append(line.strip())
        return self.listname
    def add_user(self, user_name):
        self.users.append(user_name)
    def del_user(self, user_name):
        if user_name in self.listname:
            self.listname.remove(user_name)
    def search_by_name(self, name):
        user_under_this_name = []
        for user in self.users:
            if user.name == name:
                user_under_this_name.append(user)
        return user_under_this_name
    def search_by_city(self, city):
        user_under_this_city = []
        for user in self.users:
            if user.city == city:
                user_under_this_city.append(user)
        return user_under_this_city
    def search_by_phone(self, phone):
        user_under_this_phone = []
        for user in self.users:
            if user.phone == phone:
                user_under_this_phone.append(user)
        return user_under_this_phone

class Transaction(object):
    def __init__(self, book_name, user_name, time, date, trans_type):
        Book.__init__(self,book_name)
        User.__init__(self,user_name)
        self.time = time
        self.date = date
        self.trans_type = trans_type
        self.trans = []
    def load_file(self, filename):
        self.listname = []
        self.list = open(filename,'r')
        for line in self.list:
            self.listname.append(line.strip())
        return self.listname
    def add_trans(self, book_name, user_name, time, date, trans_type):
        self.trans.append(book_name)
        self.trans.append(user_name)
        self.trans.append(time)
        self.trans.append(date)
        self.trans.append(trans_type)
    def del_trans(self, book_name, user_name, time, date):
        if book_name in self.listname:
            self.listname.remove(book_name)
        elif user_name in self.listname:
            self.listname.remove(user_name)
        elif time in self.listname:
            self.listname.remove(time)
        elif date in self.listname:
            self.listname.remove(date)
    def search_by_user_name(self, user_name):
        User.search_by_name(user_name)
    def search_by_book_name(self, book_name):
        Book.search_by_name(book_name)
    def search_by_date(self, date):
        Tra_under_this_date = []
        for date1 in self.date:
            if date1.date == date:
                Tra_under_this_date.append(date1)
            return Tra_under_this_date
            
class Library(Author,Book,User,Transaction):  #the Library class have super class of all 4 classes that we develpoed
    def __init__(self, name,quantity): # inital the value from the Book class and declear other attributes
        #Book.__init__(self,name)
        self.author = []             # set all list to empty so we can get them from pervious class
        self.users = []
        self.Books = []
        self.Transactions = []
        self.quantity = 0           # set quantity to 0 first
        self.dict = dict()          # declear the dictionary
    def load_list(self,author,users,Books,Transaction):    # load the list from last 4 class and give them values in Library class
        Library.author = Author.authors
        Library.users = User.users
        Library.Books = Book.books
        Library.Transactions = Transaction.trans
    def add_dict(self,name,quantity):          # add other books if needed to the dictionary
        self.dict.update({name:quantity})
    def update_dict(self,name, trans_type):    # update the values of each key(book name) based on Transaction type
        if Transaction.trans_type == 1:         # if borrowed value -1
            self.dict [name] -= 1
        elif Transaction.trans_type == 0:       # if returened value +1
            self.dict [name] += 1
    def search_by_name(self,name):              #search the book avaliable by book name
        for name1 in list(self.dict.keys()):
            if name1 == name:                   # return the value of that book (borrowed or returned)
                return self.dict[name]
            
    def search_by_author_name(self,author_name):     # search the book avaliable by author name 
        book_name = Book.search_by_author_name(author_name) # related to Book class and Author class
        Library.search_by_name(book_name)              # return the result value

    def search_by_author_nation(self,author_nation):    # search the book avaliable by author nationality
        book_name = Book.search_by_nationality(author_nation)  # related to Book class and Author class
        Library.search_by_name(book_name)       # return the result value

    def search_by_author_users_name(self,users_name):    # search the book avaliable by user name 
        book_name = User.search_by_name(users_name)    # related to User class
        Library.search_by_name(book_name)      # return the result value
 
    def search_by_phone(self,phone):       # search the book avaliable by user phone 
        book_name = User.search_by_name(phone)   # related to User class
        Library.search_by_name(book_name)     # return the result value

# test
author = namedtuple('author', 'name nationality date_of_birth age')   # test each class
authorss = Author('','','','')                                          # call Author class
authorss.add_author(author( 'Jeff Potter','America', '1995/04/21', 22))# add each attribuutes to it
authorss.add_author(author( 'A','China', '1999/04/21', 18))
authorss.add_author(author( 'B','Japan', '1991/02/21', 5))
authorss.add_author(author( 'C','America', '1992/03/21', 10))
print(authorss.search_by_name('B'))      # test search function by name, nation, age_range
print(authorss.search_by_natonality('Japan'))
print(authorss.search_by_agerange(20, 30))
bookss = Book('','','')     # call book class
bookss.add_book('SB')      # add one book to it which related by Author
print(bookss.books)        # see what book list
libraryss = Library('','')   # call Library class
libraryss.add_dict('SB',0)   # add each book with value
libraryss.add_dict('AB',1)
libraryss.add_dict('B',1)
libraryss.add_dict('C',0)
print(libraryss.dict)     # see the dictionary result
print(libraryss.search_by_name('AB'))   # search by book name
#print(libraryss.search_by_author_name('ZX'))  # search by author name
print(libraryss.search_by_name('C'))   # search by users name