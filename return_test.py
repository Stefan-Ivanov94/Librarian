#def no_return():
#    return ('a','b')
#
#nothing = no_return()
#if nothing:
#    print(f"Returned {nothing}")
#else:
#    print(nothing)
#def read_book()->tuple:
#    title = input("Book title:")
#    author = input("Author name:")
#    if title or author:
#        book = title, author
#        return book
#    else:
#        print("You must enter title and/or author!")
#        return read_book()
#    
#bok = read_book()
#print(bool(bok[0]))
list = []
print(bool(list))