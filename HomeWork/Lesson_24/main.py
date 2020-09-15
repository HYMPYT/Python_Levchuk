from person import Person
from functor import SortKey

def print_rez(lst: list):
    """Function for representation of person list"""
    for item in lst:
        print(item)

#! Decorator
def sort_decorator_by(key: str):
    def decorator(func):
        def wrapper(obj: Person):
            return getattr(func(obj), key)
        return wrapper
    return decorator

#! Function for sorting person list by age
@sort_decorator_by("age")
def sorting_by_age(obj: Person):
    return obj

#! Function for sorting person list by surname
@sort_decorator_by("surname")
def sorting_by_surname(obj: Person):
    return obj

if __name__ == "__main__":
    persons = [
        Person("Vasya", "Pupkin", 23),
        Person("Oleg", "Prokopovich", 54),
        Person("Ivan", "Kucher", 19),
        Person("Sasha", "Haustovich", 20),
        Person("Judgin", "Smith", 30)
    ]
    print_rez(persons)
    print("~" * 50)

    #! functor
    # persons.sort(key=SortKey("age"))

    #! lambda
    # key_sort = "age"
    # persons.sort(key=lambda x: getattr(x, key_sort))

    #! decorator
    # persons.sort(key=sorting_by_age)
    
    print_rez(persons)


#! Answer
#* Різниця між функтором і декоратором в тому, що нам потрібно постійно оголошувати нові функції для того щоб їх декорувати.
#* Функтор і лямбда схожі у використанні тому, що ми можемо замінити і лямбду і функтор замиканням.