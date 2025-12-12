import pickle

def save(books):
    try:
        with open('books.pkl', 'wb') as file:
            pickle.dump(books, file)
        return True
    except Exception as e:
        print("Error opening books.pkl:", e)
        return False

def load():
    try:
        with open('books.pkl', 'rb') as file:
            return pickle.load(file)
    except Exception as e:
        print("Error opening books.pkl:", e)
        return -1

def add_book(books):
    title = input("Title: ")
    year = input("Year: ")
    pages = input("Pages: ")
    isbn = input("ISBN: ")
    user_id = input("User id: ")

    if year.isdigit() and pages.isdigit() and user_id.isdigit():
        new_id = 1
        if len(books) > 0:
            last = books[-1]["book_id"]
            new_id = last + 1
        book = {
            "book_id": new_id,
            "title": title,
            "year_published": int(year),
            "pages": int(pages),
            "isbn": isbn,
            "user_id": int(user_id)
        }
        books.append(book)
        return True
    else:
        return False

def delete_book(books, book_id):

def find_books_by_title(books, query):

def make_menu(options):
    header = "*" * 40 + "\n" + "MENU".center(40) + "\n" + "*" * 40
    body = ""
    counter = 1
    for i in range(len(options)):
        body += str(counter) + ")" + options[i] + "\n"
        counter += 1
    while True:
        print(header)
        print(body, end="")
        option = input("-> Option: ")
        if option.isdigit():
            value = int(option)
            if value in range(1, counter):
                return value
            else:
                print("Invalid value".center(40, "="))
                input("Press Enter to continue...")
        else:
            print("Invalid value".center(40, "="))
            input("Press Enter to continue...")

Books = [
    {
        "book_id": 1,
        "title": "A Game of Thrones",
        "year_published": 1996,
        "pages": 694,
        "isbn": "978-0553103540",
        "user_id": 0
    }
]

menu_options = ["Load data", "Save data", "Add a book", "Delete a book", "Find books"]