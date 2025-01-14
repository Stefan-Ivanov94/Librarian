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
        publisher = input("Publisher:")
        year = int(input("Year of release:"))
        location = input("Location:")
        
        book = title, author
        if book in books:   #TODO: Consider adding prompts
            books[book][2] += 1
            books[book][3].append(location)
        else:
            books[book] = [publisher,year,1,location]
    elif command == "move":
        pass
    elif command == "remove":
        title = input("Book title:")
        author = input("Author name:")
        location = input("Location to remove from:")
        book = title, author
        if book not in books:
            print("Book not found. Chech title and author spelling!")
        elif location not in books[book][3]:
            print("Book not found in specified location.")
        else:
            books[book][2] -= 1
            if books[book][2] == 0:
                del books[book]
            else:
                books[book][3].remove(location)
    elif command == "search":
        pass
    else:
        print("Invalid command!")
        
    command = input()