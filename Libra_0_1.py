# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 14:08:20 2024

@author: Stefan
"""

#Dictionary to store books data
books = {} 
#commonly used prompts
main_prompt = "Do you want to: add, move, remove, search or list all book? "
not_found = "Book not found. Chech title and author spelling!"
bad_lacation = "Book not found in specified location."

def read_file(file_name:str)->dict:
    #TODO: Add docstring
    books = {}
    with open(file_name, 'r') as books_list:
        for raw_book in books_list:
            raw_book = raw_book.strip().split('|')
            book_key = raw_book[0], raw_book[1]
            locations = raw_book[4].split('+')
            book_info = [raw_book[2], int(raw_book[3]), locations]
            books[book_key] = book_info
        print(f"A total of {len(books)} unique books have been loaded")
    return books

def read_book_key()->tuple:
    title = input("Book title:")
    author = input("Author name:")
    if title or author:
        book = title, author
        return book
    else:
        print("You have to enter title and/or author!")
        return read_book_key()
    
def validate_title_and_author(book_key:tuple)->tuple:
    if not book_key[0]:
        valid_title = input("You have to enter book title! ")
        return (valid_title,book_key[1])
    elif not book_key[1]:
        valid_author = input("You have to enter author name! ")
        return (book_key[0],valid_author)
    else:
        return book_key
    
def add_book(book_key:tuple,book_location:str,books_data:dict)->dict:
    if book_key in books_data:
        books_data[book_key][2].append(book_location)
    else:
        publisher = input("Publisher:")
        year = int(input("Year of release:"))
        locations = [book_location]
        books_data[book_key] = [publisher,year,locations]
    print(f"A copy of {book_key[0]} by {book_key[1]} published by {publisher}\
         in {year} was added in {book_location}.")
    return books_data

def move_book(book_key:tuple,books_data:dict,start_location:str,end_location:str)->dict:
    if start_location in books_data[book_key][2]:
        books_data[book_key][2].remove(start_location)
        books_data[book_key][2].append(end_location)
        print(f"Book succesfuly moved from {start_location} to {end_location}")
    else:
        print(bad_lacation)
    return books_data

def remove_book(book_key:tuple,books_data:dict,location:str)->dict:
    if book_key in books_data:
        books_data[book_key][2].remove(location)
        if not books_data[book_key][2]:
            del books[book]
        print(f"{book[0]} by {book[1]} removed from {location}.")
    else:
        print(bad_lacation)
    return books_data

books = read_file('test_file_01.txt')
command = input(main_prompt)

while command != "end":  #TODO: Make list of STOP commands
    if command == "add":
        book = validate_title_and_author(read_book_key())
        location = input("Location:")
        books = add_book(book,location,books)
    elif command == "move":
        book = validate_title_and_author(read_book_key())
        if book in books:
            start_location = input("Location to move from:")
            end_location = input("Location to move to:")
            books = move_book(book,books,start_location,end_location)
        else:
            print(not_found)       
    elif command == "remove":
        book = validate_title_and_author(read_book_key())
        if book in books:
            location = input("Location to remove from:")
            books = remove_book(book,books,location)
        else:
            print(not_found)
    elif command == "search":
        print("If you want to search by author, leave title empty and vice versa.")
        book_to_find = read_book_key()
        books_found = {}
        for book, info in books.items():
            if len(title) == 0 and book[1] == author:
                books_found[book] = info
            elif len(author) == 0 and book[0] == title:
                books_found[book] = info
            elif book == (title,author):
                books_found[book] = info
        for book, info in books_found.items():
            print(f"{book[0]} by {book[1]} published by {info[0]} in {info[1]} found in {'; '.join(info[2])}.") 
        if len(books_found) == 0:
            print(not_found)
    elif command == "list all":
        list_type = input("Simple(title, author and number of copies) or detailed list? ")
        number_of_books = 0
        if list_type.lower() == "simple":
            for book,info in books.items():
                number_of_books += len(info[2])
                print(f"{book[0]} by {book[1]} ({len(info[2])})") 
        elif list_type.lower() == "detailed":
            for book,info in books.items():
                number_of_books += len(info[2])
                print(f"{book[0]} by {book[1]} Publisher: {info[0]} Year: {info[1]} Found in: {', '.join(info[2])}") 
        else:
            print("Invalid command!")
            command = input(main_prompt)
            continue
        print(f"You have {number_of_books} books of wich {len(books)} are unique.")
    else:
        print("Invalid command!")
        
    command = input(main_prompt)

with open('test_file_01.txt','w') as books_list:
    for book, info in books.items():
        book_as_list = [book[0], book[1], info[0], str(info[1]), '+'.join(info[2])]
        book_as_string = '|'.join(book_as_list) + '\n'
        books_list.write(book_as_string)