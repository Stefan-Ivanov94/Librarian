books = {}
with open('test_file_01.txt', 'r') as books_list:
    for raw_book in books_list:
        raw_book = raw_book.strip().split('|')
        book_key = raw_book[0], raw_book[1]
        locations = raw_book[4].split('+')
        book_info = [raw_book[2], int(raw_book[3]), locations]
        books[book_key] = book_info
    print(f"A total of {len(books)} books have been loaded")

number_of_books = 0
for book, info in books.items():
    number_of_books += len(info[2])
    print(f"{book[0]} by {book[1]} ({len(info[2])})")
print(f"You have {number_of_books} books of wich {len(books)} are unique.")