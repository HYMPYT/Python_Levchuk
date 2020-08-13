from pprint import pprint

def print_result(*args) -> None:
    """This function prints the elements that are passed as a parameter."""
    for element in args:
        pprint(element, width=1)
    input("Press Enter to continue...")

def add_book(author: str, title: str, genre: str, publishing_year: int, number_of_pages: int, publisher: str) -> dict:
    """This function is for adding new book to the books collection."""
    global BOOKS
    book = {
        "Author": author,
        "Title": title,
        "Genre": genre,
        "Publishing year": publishing_year,
        "Number of pages": number_of_pages,
        "Publisher": publisher
    }
    BOOKS.append(book)
    return book

def del_book(title: str) -> dict:
    """This function is for deleting book.
    The key to the search is the title of the book."""
    global BOOKS
    del_book = {}
    for index, book in enumerate(BOOKS):
        if book["Title"] == title:
            del_book = book
            del(BOOKS[index])
            return del_book

def edit_fields(book: dict) -> tuple:
    """This function is for editing the book information fields."""
    fields = []

    author = book["Author"]
    title = book["Title"]
    genre = book["Genre"]
    publishing_year = book["Publishing year"]
    number_of_pages = book["Number of pages"]
    publisher = book["Publisher"]

    new_author = input(f"Enter author ({author} - default): ")
    new_title = input(f"Enter title ({title} - default): ")
    new_genre = input(f"Enter genre ({genre} - default): ")
    new_publisher = input(f"Enter pulisher ({publisher} - default): ")

    try:
        new_publishing_year = int(input(f"Enter publishing year ({publishing_year} - default): "))
        book["Publishing year"] = new_publishing_year
        fields.append("Publishing year")
    except ValueError as e:
        print(f'\nError: {e}.\nField "Publishing year" not changed.\n')
        input("Press Enter to continue...")
    try:
        new_number_of_pages = int(input(f"Enter number of pages ({number_of_pages} - default): "))
        book["Number of pages"] = new_number_of_pages
        fields.append("Number of pages")
    except ValueError as e:
        print(f'\nError: {e}.\nField "Number of pages" not changed.\n')
        input("Press Enter to continue...")

    if new_author:
        book["Author"] = new_author
        fields.append("Author")
    if new_title:
        book["Title"] = new_title
        fields.append("Title")
    if new_genre:
        book["Genre"] = new_genre
        fields.append("Genre")
    if new_publisher:
        book["Publisher"] = new_publisher
        fields.append("Publisher")

    return book, fields

def update_book(title: str) -> dict:
    """This function is for editing the book.
    The key to the search is the title of the book."""
    global BOOKS
    for book in BOOKS:
        if book["Title"] == title:
            update_book = edit_fields(book)
            for field in update_book[1]:
                book[field] = update_book[0][field]
            return book

def search_book(title: str) -> dict:
    """This function for search book.
    The key to the search is the title of the book."""
    global BOOKS
    for book in BOOKS:
        if book["Title"] == title:
            return book
    return f"Book {title} does not exist\n"


if __name__ == "__main__":
    # ! CONSTS
    BOOKS_LIST = 'list'
    ADD_BOOK = 'add'
    DEL_BOOK = 'delete'
    UPDATE_BOOK = 'update'
    SEARCH_BOOK = 'search'
    EXIT = 'q'
    BOOKS = [
        {
            "Author": "Stephen_King",
            "Title": "Cujo",
            "Genre": "Horror",
            "Publishing year": 1981,
            "Number of pages": 319,
            "Publisher": "Viking_Press"
        },
        {
            "Author": "Stephen_King",
            "Title": "The_Shining",
            "Genre": "Horror",
            "Publishing year": 1977,
            "Number of pages": 447,
            "Publisher": "Doubleday"
        }
    ]

    while True:
        print(f'''
        Choices:
        BOOKS_LIST -> {BOOKS_LIST}
        ADD_BOOK -> {ADD_BOOK}
        DEL_BOOK -> {DEL_BOOK}
        UPDATE_BOOK -> {UPDATE_BOOK}
        SEARCH_BOOK -> {SEARCH_BOOK}
        EXIT -> {EXIT}
        ---------------------
        ''')

        choice = input('Enter choice: ')
        if choice == EXIT:
            break

        elif choice == BOOKS_LIST:
            if len(BOOKS) > 1:
                print("\n~~~~~~~ Books ~~~~~~~")
            else:
                print("\n~~~~~~~ Book ~~~~~~~")
            print_result(BOOKS)

        elif choice == ADD_BOOK:
            author = input('Enter author: ')
            title = input('Enter title: ')
            genre = input('Enter genre: ')
            publisher = input('Enter publisher: ')
            try:
                publishing_year = int(input('Enter publishing year: '))
            except ValueError as e:
                publishing_year = 0
                print(f'\nError: {e}.\nFor field "Publishing year" was used default value: 0.\nIf you want to change it use the command "update"\n')
                input("\nPress Enter to continue...")
            try:
                number_of_pages = int(input('Enter number of pages: '))
            except ValueError as e:
                number_of_pages = 0
                print(f'\nError: {e}.\nFor field "Number of pages" was used default value: 0.\nIf you want to change it use the command "update"\n')
                input("\nPress Enter to continue...")
            
            book = add_book(
                author=author,
                title=title,
                genre=genre,
                publishing_year=publishing_year,
                publisher=publisher,
                number_of_pages=number_of_pages
            )
            print("\n~~~~~~~ Book ~~~~~~~")
            print_result(book)

        elif choice == DEL_BOOK:
            title = input("Enter title: ")
            book = del_book(title=title)
            print("\n~~~~~~~ Book ~~~~~~~")
            print_result(book)

        elif choice == UPDATE_BOOK:
            title = input("Enter title: ")
            book = update_book(title=title)
            print("\n~~~~~~~ Book ~~~~~~~")
            print_result(book)

        elif choice == SEARCH_BOOK:
            title = input("Enter title: ")
            book = search_book(title=title)
            print("\n~~~~~~~ Book ~~~~~~~")
            print_result(book)

        else:
            print("Entered wrong data. Please try again.")
            input("Press Enter to continue...")