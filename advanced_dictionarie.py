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
        if book in books:   #TODO: Move afte author is initiated to improve user expirience Consider adding prompts
            books[book][2].append(location)
        else:
            locations = [location]
            books[book] = [publisher,year,locations]
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
        search_type = input("Search by author, by title or by both?")
        if search_type.lower() == "author":
            pass
        elif search_type.lower() == "title":
            pass
        elif search_type.lower() == "both":
            title = input("Book title:")
            author = input("Author name:")
            desired_book = title,author
            for book in books: # Breaks after first find
                if book == desired_book:
                    print(book)
        else:
            print("Only \"author\", \"title\" or \"both\" are valid commands.")
    else:
        print("Invalid command!")
        
    command = input("Do you want to: add, move, remove or search a book?")