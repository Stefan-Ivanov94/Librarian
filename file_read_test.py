books = {}
with open('test_file_01.txt', 'r') as books_list:
    for raw_book in books_list:
        raw_book = raw_book.strip().split('|')
        key = tuple(raw_book[0].split('+'))
        raw_value = raw_book[1].split(',')
        locations = raw_value[2].split('+')
        value = [raw_value[0], raw_value[1], locations]
        books[key] = value

number_of_books = 0
for book, info in books.items():
    number_of_books += len(info[2])
    print(f"{book[0]} by {book[1]}")
print(f"You have {number_of_books} books of wich {len(books)} are unique.")