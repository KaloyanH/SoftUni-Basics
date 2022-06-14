favourite_book = input()

checked_books = -1
book_in_library = ""
while book_in_library != favourite_book:
    book_in_library = input()
    checked_books += 1
    if book_in_library == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {checked_books} books.")
        break
    elif book_in_library == favourite_book:
        print(f"You checked {checked_books} books and found it.")
        break




