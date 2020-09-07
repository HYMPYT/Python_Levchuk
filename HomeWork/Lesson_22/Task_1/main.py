from coffee_machine import CoffeeMachine
from blender import Blender
from meat_grinder import MeatGrinder


if __name__ == "__main__":
    #! CONSTS
    COFFEE_MACHINE = "coffee"
    BLENDER = "blender"
    MEAT_GRINDER = "meat"
    CREATE_OBJECT = "create"
    PRINT_OBJECT = "display"
    EDIT_FIELDS = "edit"
    EXIT = "q"

    while True:
        print(f"""
        Choices:
            COFFEE_MACHINE -> {COFFEE_MACHINE}
            BLENDER -> {BLENDER}
            MEAT_GRINDER -> {MEAT_GRINDER}
            EXIT -> {EXIT}
        ------------------------
        """)
        choice = input('Enter choice: ')

        if choice == EXIT:
            break

        elif choice == COFFEE_MACHINE:
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
                    manufacturer = input("Enter the manufacturer of the coffee machine: ")

                    model = input("Enter the coffee machine model: ")

                    power = input("Enter the power of the coffee machine: ")

                    coffee_machine = CoffeeMachine(manufacturer=manufacturer, model=model, power=power)

                    print(coffee_machine)
                    input("Press Enter to continue...")

                elif choice == PRINT_OBJECT:
                    try:
                        print(coffee_machine)
                    except NameError:
                        print("Error: Please create the object of the coffee machine")
                    input("Press Enter to continue...")

                elif choice == EDIT_FIELDS:
                    try:
                        coffee_machine.manufacturer = input(f"Enter the manufacturer of the coffee machine ({coffee_machine.manufacturer} - default): ")

                        coffee_machine.model = input(f"Enter the coffee machine model ({coffee_machine.model} - default): ")

                        coffee_machine.power = input(f"Enter the power of the coffee_machine ({coffee_machine.power} - default): ")

                        print(coffee_machine)
                    except NameError:
                        print("Error: Please create the object of the coffee machine")

                    input("Press Enter to continue...")

                else:
                    print("Entered wrong data. Please try again.")
                    input("Press Enter to continue...")

        elif choice == BLENDER:
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

                    manufacturer = input("Enter the manufacturer of the blender: ")

                    blender_type = input("Enter the blender type: ")

                    blender = Blender(manufacturer=manufacturer, blender_type=blender_type)

                    print(blender)
                    input("Press Enter to continue...")

                elif choice == PRINT_OBJECT:
                    try:
                        print(blender)
                    except NameError:
                        print("Error: Please create the object of the blender")
                    input("Press Enter to continue...")


                elif choice == EDIT_FIELDS:
                    try:
                        blender.manufacturer = input(f"Enter the manufacturer of the blender ({blender.manufacturer} - default): ")

                        blender.blender_type = input(f"Enter the blender type ({blender.blender_type} - default): ")

                        print(blender)
                    except NameError:
                        print("Error: Please create the object of the blender")
                    input("Press Enter to continue...")

                else:
                    print("Entered wrong data. Please try again.")
                    input("Press Enter to continue...")

        elif choice == MEAT_GRINDER:
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
                    manufacturer = input("Enter the manufacturer of the meat grinder: ")

                    meat_grinder_type = input("Enter the meat grinder type: ")
                    
                    meat_grinder = MeatGrinder(manufacturer=manufacturer, meat_grinder_type=meat_grinder_type)

                    print(meat_grinder)
                    input("Press Enter to continue...")

                elif choice == PRINT_OBJECT:
                    try:
                        print(meat_grinder)
                    except NameError:
                        print("Error: Please create the object of the meat grinder")
                    input("Press Enter to continue...")

                elif choice == EDIT_FIELDS:
                    try:
                        meat_grinder.manufacturer = input(f"Enter the manufacturer of the meat grinder ({meat_grinder.manufacturer} - default): ")

                        meat_grinder.meat_grinder_type = input(f"Enter the meat grinder type ({meat_grinder.meat_grinder_type} - default): ")

                        print(meat_grinder)
                    except NameError:
                        print("Error: Please create the object of the meat grinder")
                    input("Press Enter to continue...")

                else:
                    print("Entered wrong data. Please try again.")
                    input("Press Enter to continue...")

        else:
            print("Entered wrong data. Please try again.")
            input("Press Enter to continue...")