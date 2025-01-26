command = input()
books = {}
while command != "end":
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
    command = input()

with open('test_file_01.txt','w') as books_list:
    for book, info in books:
        book_as_string = f"{book[0]}-{book[1]}:{info[0]},{info[1]},{'+'.join(info[2])}\n" 
        books_list.write(book_as_string)