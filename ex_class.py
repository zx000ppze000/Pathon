# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 11:13:55 2018

@author: zhangx
"""

from collections import namedtuple


class Library(object):
    def __init__(self):
        self.books = []

    def addBook(self, book):
        self.books.append(book)

    def searchBookISBN(self, ISBN):
        for book in self.books:
            if book.ISBN == ISBN:
                return book

    def searchBookAuthor(self, author):
        written_by_author = []
        for book in self.books:
            if book.author == author:
                written_by_author.append(book)
        return written_by_author

    def searchUnderPrice(self, price):
        books_under_price = []
        for book in self.books:
            if book.price < price:
                books_under_price.append(book)
        return books_under_price


Book = namedtuple('Book', 'name author ISBN price')

library = Library()
library.addBook(Book('Geometry', 'Jeff Potter', '0596805888', 22))
library.addBook(Book('Math', 'George Harr', '0594805888', 15))
library.addBook(Book('English', 'James Odd', '0596225888', 10))
library.addBook(Book('Physics', 'Jeff Potter', '0597884512', 18))
print(library.searchBookISBN('0594805888'))
print(library.searchBookAuthor('George Harr'))
print(library.searchUnderPrice(20))