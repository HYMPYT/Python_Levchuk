from car import Car
from book import Book
from stadium import Stadium
from datetime import date


if __name__ == "__main__":
    #! CONSTS
    TASK_1 = "car"
    TASK_2 = "book"
    TASK_3 = "stadium"
    CREATE_OBJECT = "create"
    PRINT_OBJECT = "display"
    EDIT_FIELDS = "edit"
    EXIT = "q"

    while True:
        print(f"""
        Choices:
            TASK_1 -> {TASK_1}
            TASK_2 -> {TASK_2}
            TASK_3 -> {TASK_3}
            EXIT -> {EXIT}
        ------------------------
        """)
        choice = input('Enter choice: ')

        if choice == EXIT:
            break

        elif choice == TASK_1:
            while True:
                print(f"""
                Choices:
                    CREATE_OBJECT -> {CREATE_OBJECT}
                    PRINT_OBJECT -> {PRINT_OBJECT}
                    EDIT_FIELDS -> {EDIT_FIELDS}
                    EXIT -> {EXIT}
                ------------------------
                """)
                choice = input("Enter choice: ")

                if choice == EXIT:
                    break

                elif choice == CREATE_OBJECT:
                    car = Car()

                    print("All data is optional")
                    model = input("Enter the car model: ")
                    if model:
                        car.model = model

                    year = input("Enter the year of the car: ")
                    if year:
                        car.year = year

                    manufacturer = input("Enter the manufacturer of the car: ")
                    if manufacturer:
                        car.manufacturer = manufacturer

                    volume = input("Enter the engine volume of the car: ")
                    if volume:
                        car.volume = volume

                    color = input("Enter the color of the car: ")
                    if color:
                        car.color = color

                    price = input("Enter the price of the car: ")
                    if price:
                        car.price = price

                    print(car)
                    input("Press Enter to continue...")

                elif choice == PRINT_OBJECT:
                    try:
                        print(car)
                    except NameError:
                        print("Error: Please create the object of the car")
                    input("Press Enter to continue...")

                elif choice == EDIT_FIELDS:
                    try:
                        model = input(f"Enter the car model ({car.model} - default): ")
                        if model:
                            car.model = model

                        year = input(f"Enter the year of the car ({car.year} - default): ")
                        if year:
                            car.year = year

                        manufacturer = input(f"Enter the manufacturer of the car ({car.manufacturer} - default): ")
                        if manufacturer:
                            car.manufacturer = manufacturer

                        volume = input(f"Enter the engine volume of the car ({car.volume} - default): ")
                        if volume:
                            car.volume = volume

                        color = input(f"Enter the color of the car ({car.color} - default): ")
                        if color:
                            car.color = color

                        price = input(f"Enter the price of the car ({car.price} - default): ")
                        if price:
                            car.price = price

                        print(car)
                    except NameError:
                        print("Error: Please create the object of the car")

                    input("Press Enter to continue...")

                else:
                    print("Entered wrong data. Please try again.")
                    input("Press Enter to continue...")

        elif choice == TASK_2:
            while True:
                print(f"""
                Choices:
                    CREATE_OBJECT -> {CREATE_OBJECT}
                    PRINT_OBJECT -> {PRINT_OBJECT}
                    EDIT_FIELDS -> {EDIT_FIELDS}
                    EXIT -> {EXIT}
                ------------------------
                """)
                choice = input("Enter choice: ")

                if choice == EXIT:
                    break

                elif choice == CREATE_OBJECT:
                    book = Book()

                    print("All data is optional")
                    title = input("Enter the title of the book: ")
                    if title:
                        book.title = title

                    year = input("Enter the year of the book: ")
                    if year:
                        book.year = year

                    publisher = input("Enter the publisher of the book: ")
                    if publisher:
                        book.publisher = publisher

                    genre = input("Enter the genre of the book: ")
                    if genre:
                        book.genre = genre
                    
                    author = input("Enter the author of the book: ")
                    if author:
                        book.author = author

                    price = input("Enter the price of the book: ")
                    if price:
                        book.price = price

                    print(book)
                    input("Press Enter to continue...")

                elif choice == PRINT_OBJECT:
                    try:
                        print(book)
                    except NameError:
                        print("Error: Please create the object of the book")
                    input("Press Enter to continue...")


                elif choice == EDIT_FIELDS:
                    try:
                        title = input(f"Enter the title of the book ({book.title} - default): ")
                        if title:
                            book.title = title

                        year = input(f"Enter the year of the book ({book.year} - default): ")
                        if year:
                            book.year = year

                        publisher = input(f"Enter the publisher of the book ({book.publisher} - default): ")
                        if publisher:
                            book.publisher = publisher

                        genre = input(f"Enter the genre of the book ({book.genre} - default): ")
                        if genre:
                            book.genre = genre
                        
                        author = input(f"Enter the author of the book ({book.author} - default): ")
                        if author:
                            book.author = author

                        price = input(f"Enter the price of the book ({book.price} - default): ")
                        if price:
                            book.price = price

                        print(book)
                    except NameError:
                        print("Error: Please create the object of the book")
                    input("Press Enter to continue...")

                else:
                    print("Entered wrong data. Please try again.")
                    input("Press Enter to continue...")

        elif choice == TASK_3:
            while True:
                print(f"""
                Choices:
                    CREATE_OBJECT -> {CREATE_OBJECT}
                    PRINT_OBJECT -> {PRINT_OBJECT}
                    EDIT_FIELDS -> {EDIT_FIELDS}
                    EXIT -> {EXIT}
                ------------------------
                """)
                choice = input("Enter choice: ")

                if choice == EXIT:
                    break

                elif choice == CREATE_OBJECT:
                    stadium = Stadium()

                    print("All data is optional")
                    name = input("Enter the name of the stadium: ")
                    if name:
                        stadium.name = name

                    opening_date = input("Enter the stadium opening date (YYYY-MM-DD): ")
                    if opening_date:
                        try:
                            stadium.opening_date = date.fromisoformat(opening_date)
                        except ValueError:
                            print("\nError: please enter the date in right format.\n")
                    
                    country = input("Enter the country of the stadium: ")
                    if country:
                        stadium.country = country

                    city = input("Enter the city of the stadium: ")
                    if city:
                        stadium.city = city

                    capacity = input("Enter stadium capacity: ")
                    if capacity:
                        stadium.capacity = capacity

                    print(stadium)
                    input("Press Enter to continue...")

                elif choice == PRINT_OBJECT:
                    try:
                        print(stadium)
                    except NameError:
                        print("Error: Please create the object of the stadium")
                    input("Press Enter to continue...")

                elif choice == EDIT_FIELDS:
                    try:
                        name = input(f"Enter the name of the stadium ({stadium.name} - default): ")
                        if name:
                            stadium.name = name

                        opening_date = input(f"Enter the stadium opening date ({stadium.opening_date} - default) (YYYY-MM-DD): ")
                        if opening_date:
                            try:
                                stadium.opening_date = date.fromisoformat(opening_date)
                            except ValueError:
                                print("\nError: please enter the date in right format.\n")
                        
                        country = input(f"Enter the country of the stadium ({stadium.country} - default): ")
                        if country:
                            stadium.country = country

                        city = input(f"Enter the city of the stadium ({stadium.city} - default): ")
                        if city:
                            stadium.city = city

                        capacity = input(f"Enter stadium capacity ({stadium.capacity} - default): ")
                        if capacity:
                            stadium.capacity = capacity

                        print(stadium)
                    except NameError:
                        print("Error: Please create the object of the stadium")
                    input("Press Enter to continue...")

                else:
                    print("Entered wrong data. Please try again.")
                    input("Press Enter to continue...")

        else:
            print("Entered wrong data. Please try again.")
            input("Press Enter to continue...")

                