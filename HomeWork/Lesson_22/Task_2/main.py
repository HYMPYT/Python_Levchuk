from frigate import Frigate
from destroyer import Destroyer
from cruiser import Cruiser


if __name__ == "__main__":
    #! CONSTS
    FRIGATE = "frigate"
    DESTROYER = "destroyer"
    CRUISER = "cruiser"
    CREATE_OBJECT = "create"
    PRINT_OBJECT = "display"
    EDIT_FIELDS = "edit"
    EXIT = "q"

    while True:
        print(f"""
        Choices:
            FRIGATE -> {FRIGATE}
            DESTROYER -> {DESTROYER}
            CRUISER -> {CRUISER}
            EXIT -> {EXIT}
        ------------------------
        """)
        choice = input('Enter choice: ')

        if choice == EXIT:
            break

        elif choice == FRIGATE:
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
                    print("All data is optional")
                    load_capacity = input("Enter the load capacity of the frigate: ")

                    speed = input("Enter the speed of the frigate: ")

                    name = input("Enter the name of the frigate: ")

                    housing_material = input("Enter the housing material of the frigate: ")

                    frigate = Frigate(load_capacity=load_capacity, speed=speed, name=name, housing_material=housing_material)

                    print(frigate)
                    input("Press Enter to continue...")

                elif choice == PRINT_OBJECT:
                    try:
                        print(frigate)
                    except NameError:
                        print("Error: Please create the object of the frigate")
                    input("Press Enter to continue...")

                elif choice == EDIT_FIELDS:
                    try:
                        frigate.load_capacity = input(f"Enter the load capacity of the frigate ({frigate.load_capacity} - default): ")

                        frigate.speed = input(f"Enter the speed of the frigate ({frigate.speed} - default): ")

                        frigate.name = input(f"Enter the name of the frigate ({frigate.name} - default): ")

                        frigate.housing_material = input(f"Enter the housing material of the frigate ({frigate.housing_material} - default): ")

                        print(frigate)
                    except NameError:
                        print("Error: Please create the object of the frigate")

                    input("Press Enter to continue...")

                else:
                    print("Entered wrong data. Please try again.")
                    input("Press Enter to continue...")

        elif choice == DESTROYER:
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
                    print("All data is optional")

                    load_capacity = input("Enter the load capacity of the destroyer: ")

                    speed = input("Enter the speed of the destroyer: ")

                    name = input("Enter the name of the destroyer: ")

                    count_of_mines = input("Enter the count of mines of the destroyer: ")

                    destroyer = Destroyer(load_capacity=load_capacity, speed=speed, name=name, count_of_mines=count_of_mines)

                    print(destroyer)
                    input("Press Enter to continue...")

                elif choice == PRINT_OBJECT:
                    try:
                        print(destroyer)
                    except NameError:
                        print("Error: Please create the object of the destroyer")
                    input("Press Enter to continue...")


                elif choice == EDIT_FIELDS:
                    try:
                        destroyer.load_capacity = input(f"Enter the load capacity of the destroyer ({destroyer.load_capacity} - default): ")

                        destroyer.speed = input(f"Enter the speed of the destroyer ({destroyer.speed} - default): ")

                        destroyer.name = input(f"Enter the name of the destroyer ({destroyer.name} - default): ")

                        destroyer.count_of_mines = input(f"Enter the count of mines of the destroyer ({destroyer.count_of_mines} - default): ")

                        print(destroyer)
                    except NameError:
                        print("Error: Please create the object of the destroyer")
                    input("Press Enter to continue...")

                else:
                    print("Entered wrong data. Please try again.")
                    input("Press Enter to continue...")

        elif choice == CRUISER:
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
                    print("All data is optional")

                    load_capacity = input("Enter the load capacity of the cruiser: ")

                    speed = input("Enter the speed of the cruiser: ")

                    name = input("Enter the name of the cruiser: ")

                    classification = input("Enter the classification of the cruiser: ")

                    cruiser = Cruiser(load_capacity=load_capacity, speed=speed, name=name, classification=classification)

                    print(cruiser)
                    input("Press Enter to continue...")

                elif choice == PRINT_OBJECT:
                    try:
                        print(cruiser)
                    except NameError:
                        print("Error: Please create the object of the cruiser")
                    input("Press Enter to continue...")

                elif choice == EDIT_FIELDS:
                    try:
                        cruiser.load_capacity = input(f"Enter the load capacity of the cruiser ({cruiser.load_capacity} - default): ")

                        cruiser.speed = input(f"Enter the speed of the cruiser ({cruiser.speed} - default): ")

                        cruiser.name = input(f"Enter the name of the cruiser ({cruiser.name} - default): ")

                        cruiser.classification = input(f"Enter the classification of the cruiser ({cruiser.classification} - default): ")

                        print(cruiser)
                    except NameError:
                        print("Error: Please create the object of the cruiser")
                    input("Press Enter to continue...")

                else:
                    print("Entered wrong data. Please try again.")
                    input("Press Enter to continue...")

        else:
            print("Entered wrong data. Please try again.")
            input("Press Enter to continue...")