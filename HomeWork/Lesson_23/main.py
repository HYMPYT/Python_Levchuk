from employee import Employee
from student import Student
from person import Person


if __name__ == "__main__":
    people = [
        Student(name="Bob", age=19, university="Harvard"), 
        Person(name="Tom", age=23),
        Employee(name="Sam", age=35, position="Programmer")]
 
    for person in people:
        person.display_info()
        print()