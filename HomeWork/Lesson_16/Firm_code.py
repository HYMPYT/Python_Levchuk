from pprint import pprint

def print_result(*args) -> None:
    """This function prints the elements that are passed as a parameter."""
    for element in args:
        pprint(element, width=1)
    input("Press Enter to continue...")

def add_employee(first_name: str, surname: str, middle_name: str, phone_number: str, email: str, position: str, office_number: int, skype: str) -> dict:
    """This function is for adding employee."""
    global EMPLOYEES
    employee = {
        "First name": first_name,
        "Surname": surname,
        "Middle name": middle_name,
        "Phone number": phone_number,
        "Email": email,
        "Position": position,
        "Office number": office_numer,
        "Skype": skype
    }
    EMPLOYEES.append(employee)
    return employee

def del_employee(surname: str) -> dict:
    """This function is for deleting employee.
    The key to the search is the surname of the employee."""
    global EMPLOYEES
    del_employee = {}
    for index, employee in enumerate(EMPLOYEES):
        if employee["Surname"] == surname:
            del_employee = employee
            del(EMPLOYEES[index])
            return del_employee

def edit_fields(employee: dict) -> tuple:
    """This function is for editing the employee information fields."""
    fields = []

    first_name = employee["First name"]
    surname = employee["Surname"]
    middle_name = employee["Middle name"]
    phone_number = employee["Phone number"]
    email = employee["Email"]
    position = employee["Position"]
    skype = employee["Skype"]
    office_number = employee["Office number"]

    new_first_name = input(f"Enter first name ({first_name} - default): ")
    new_surname = input(f"Enter surname ({surname} - default): ")
    new_middle_name = input(f"Enter middle name ({middle_name} - default): ")
    new_phone_number = input(f"Enter phone number ({phone_number} - default): ")
    new_email = input(f"Enter email ({email} - default): ")
    new_position = input(f"Enter position ({position} - default): ")
    new_skype = input(f"Enter skype ({skype} - default): ")
    try:
        new_office_number = int(input(f"Enter office number ({office_number} - default): "))
        employee["Office number"] = new_office_number
        fields.append("Office number")
    except ValueError as e:
        print(f'\nError: {e}.\nField "Office number" not changed.\n')
        input("Press Enter to continue...")

    if new_first_name:
        employee["First name"] = new_first_name
        fields.append("First name")
    if new_surname:
        employee["Surname"] = new_surname
        fields.append("Surname")
    if new_middle_name:
        employee["Middle name"] = new_middle_name
        fields.append("Middle name")
    if new_phone_number:
        employee["Phone number"] = new_phone_number
        fields.append("Phone number")
    if new_email:
        employee["Email"] = new_email
        fields.append("Email")
    if new_position:
        employee["Position"] = new_position
        fields.append("Position")
    if new_skype:
        employee["Skype"] = new_skype
        fields.append("Skype")

    return employee, fields

def update_employee(surname: str) -> dict:
    """This function is for editing the employee.
    The key to the search is the surname of the employee."""
    global EMPLOYEES
    for employee in EMPLOYEES:
        if employee["Surname"] == surname:
            update_employee = edit_fields(employee)
            for field in update_employee[1]:
                employee[field] = update_employee[0][field]
            return employee

def search_employee(surname: str) -> dict:
    """This function for search employee.
    The key to the search is the surname of the employee."""
    global EMPLOYEES
    for employee in EMPLOYEES:
        if employee["Surname"] == surname:
            return employee
    return f"Employee {surname} does not exist\n"


if __name__ == "__main__":
    # ! CONSTS
    EMPLOYEES_LIST = 'list'
    ADD_EMPLOYEE = 'add'
    DEL_EMPLOYEE = 'delete'
    UPDATE_EMPLOYEE = 'update'
    SEARCH_EMPLOYEE = 'search'
    EXIT = 'q'
    EMPLOYEES = [
        {
            "First name": "Petya",
            "Surname": "Haustovuch",
            "Middle name": "Ivanovuch",
            "Phone number": "+380970162137",
            "Email": "petya228@gmail.com",
            "Position": "programmer",
            "Office number": 123,
            "Skype": "petyaIvan228"
        },
        {
            "First name": "Stanislav",
            "Surname": "Nepochatuh",
            "Middle name": "Olegovuch",
            "Phone number": "+380963458917",
            "Email": "stas2016@ukr.net",
            "Position": "accountant",
            "Office number": 243,
            "Skype": "statAccountant"
        }
    ]

    while True:
        print(f'''
        Choices:
        EMPLOYEES_LIST -> {EMPLOYEES_LIST}
        ADD_EMPLOYEE -> {ADD_EMPLOYEE}
        DEL_EMPLOYEE -> {DEL_EMPLOYEE}
        UPDATE_EMPLOYEE -> {UPDATE_EMPLOYEE}
        SEARCH_EMPLOYEE -> {SEARCH_EMPLOYEE}
        EXIT -> {EXIT}
        ---------------------
        ''')

        choice = input('Enter choice: ')
        if choice == EXIT:
            break

        elif choice == EMPLOYEES_LIST:
            if len(EMPLOYEES) > 1:
                print("\n~~~~~~ Employees ~~~~~~")
            else:
                print("\n~~~~~~ Employee ~~~~~~")
            print_result(EMPLOYEES)

        elif choice == ADD_EMPLOYEE:
            first_name = input('Enter first name: ')
            surname = input('Enter surname: ')
            middle_name = input('Enter middle name: ')
            phone_number = input('Enter phone number: ')
            email = input('Enter email: ')
            position = input('Enter position: ')
            skype = input('Enter skype: ')
            try:
                office_numer = int(input('Enter office number: '))
            except ValueError as e:
                office_numer = 0
                print(f'\nError: {e}.\nFor office number was used default value: 0.\nIf you want to change it use the command "update"\n')
                input("\nPress Enter to continue...")
            
            employee = add_employee(
                first_name=first_name,
                surname=surname,
                middle_name=middle_name,
                phone_number=phone_number,
                email=email,
                position=position,
                skype=skype,
                office_number=office_numer
            )
            print("\n~~~~~~ Employee ~~~~~~")
            print_result(employee)

        elif choice == DEL_EMPLOYEE:
            surname = input("Enter surname: ")
            employee = del_employee(surname=surname)
            print("\n~~~~~~ Employee ~~~~~~")
            print_result(employee)

        elif choice == UPDATE_EMPLOYEE:
            surname = input("Enter surname: ")
            employee = update_employee(surname=surname)
            print("\n~~~~~~ Employee ~~~~~~")
            print_result(employee)

        elif choice == SEARCH_EMPLOYEE:
            surname = input("Enter surname: ")
            employee = search_employee(surname=surname)
            print("\n~~~~~~ Employee ~~~~~~")
            print_result(employee)

        else:
            print("Entered wrong data. Please try again.")
            input("Press Enter to continue...")