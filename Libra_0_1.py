# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 14:08:20 2024

@author: Stefan
"""

books = {}      #TODO: Add file reader
main_prompt = "Do you want to: add, move, remove, search or list all book? "
command = input(main_prompt)

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
        title = input("Book title:")
        author = input("Author name:")
        book = title, author
        if book not in books:
            print("Book not found. Chech title and author spelling!")
            command = input(main_prompt)
            continue
        start_location = input("Location to move from:")
        end_location = input("Location to move to:")
        if start_location not in books[book][2]:
            print("Book not found in specified location.")
        else:
            books[book][2].remove(start_location)
            books[book][2].append(end_location)
            print(f"Book succesfuly moved from {start_location} to {end_location}")
    elif command == "remove":
        title = input("Book title:")
        author = input("Author name:")
        book = title, author
        if book not in books:
            print("Book not found. Chech title and author spelling!")
            command = input(main_prompt)
            continue
        location = input("Location to remove from:")
        if location not in books[book][2]:
            print("Book not found in specified location.")
        else:
            books[book][2].remove(location)
            if len(books[book][2]) == 0:
                del books[book]
            print(f"{book[0]} by {book[1]} removed from {location}.")
    elif command == "search":
        print("If you want to search by author, leave title empty and vice versa.")
        title = input("Book title:")
        author = input("Author name:")
        if len(title) == 0 and len(author) == 0:
            print("You have to enter title and/or author!")
            command = input(main_prompt)
            continue
        books_found = {}
        for book, info in books.items():
            if len(title) == 0 and book[1] == author:
                books_found[book] = info
            elif len(author) == 0 and book[0] == title:
                books_found[book] = info
            elif book == (title,author):
                books_found[book] = info
        for book, info in books_found.items():
            print(f"{book[0]} by {book[1]} published by {info[0]} in {info[1]} found in {info[2]}") 
    else:
        print("Invalid command!")
        
    command = input(main_prompt)