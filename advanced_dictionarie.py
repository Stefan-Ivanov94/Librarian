# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 14:08:20 2024

@author: Stefan
"""

books = {}      #TODO: Add file reader
command = input("Do you want to: add, move, remove or search a book?")

while command != "end":  #TODO: Make list of STOP commands
    if command == "add":
        title = input("Book title:")
        author = input("Author name:")
        location = input("Location:")
        book = title, author
        if book in books:
            books[book][2].append(location)
        else:
            locations = [location]
            publisher = input("Publisher:")
            year = int(input("Year of release:"))
            books[book] = [publisher,year,locations]
        print(f"A copy of {title} by {author} published by {publisher} in {year} was added in {location}.")
    elif command == "move":
        pass
    elif command == "remove":
        title = input("Book title:")
        author = input("Author name:")
        location = input("Location to remove from:")
        book = title, author
        if book not in books:
            print("Book not found. Chech title and author spelling!")
        elif location not in books[book][2]:
            print("Book not found in specified location.")
        else:
            books[book][2].remove(location)
            if len(books[book][2]) == 0:
                del books[book]
    elif command == "search":
        print("If you want to search by author, leave title empty and vice versa.")
        title = input("Book title:")
        author = input("Author name:")
        if len(title) == 0 and len(author) == 0:
            print("You have to enter title and/or author!")
            continue
        for book, info in books.items():
            #TODO: Fix locations' printing!!! And find a way to use a single print statement
            if len(title) == 0 and book[1] == author:
                print(f"{book[0]} by {book[1]} found in {locations}") 
            elif len(author) == 0 and book[0] == title:
                print(f"{book[0]} by {book[1]} found in {locations}") 
            elif book == (title,author):
                print(f"{book[0]} by {book[1]} found in {locations}")
    else:
        print("Invalid command!")
        
    command = input("Do you want to: add, move, remove or search a book?")