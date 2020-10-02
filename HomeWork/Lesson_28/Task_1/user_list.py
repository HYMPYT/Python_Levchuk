from data import Data


class UserList:
    def __init__(self, *args):
        self.__user_list = list(args)


# * Service methods
# * ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __confirm(self, mode: int) -> bool:
        """Confirmation messages"""
        if mode == Data.ADD:
            print("Element exists in list!")
            user_input = input("Confirm operation (yes): ")

        elif mode == Data.EDIT:
            print("More than 1 element in list!")
            user_input = input("Replace all accurrences? (yes): ")

        elif mode == Data.SHOW:
            user_input = input("Want to see the list from the end? (yes): ")

        elif mode == Data.DELETE:
            user_input = input("Do you confirm the operation of deleting? (yes): ")

        return True if user_input == 'yes' else False

    def __get_index_positions(self, value: int) -> list:
        """Returns list of indexes which are in stack"""
        index_list = []
        index_pos = 0
        while True:
            try:
                # Search item in list from index_pos to the end
                index_pos = self.__user_list.index(value, index_pos)
                index_list.append(index_pos)
                index_pos += 1
            except ValueError:
                break
        return index_list


# * Common methods
# * ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def add(self, number: int) -> int or None:
        """Add number to stack"""
        if number not in self.__user_list:
            self.__user_list.append(number)
            return number
        if number in self.__user_list and self.__confirm(mode=Data.ADD):
            self.__user_list.append(number)
            return number

    def edit(self, a: int, b: int) -> int or list:
        """Replace stack[a, a, ...] with b
        a: first number, b - number to replace
        """
        if not a in self.__user_list:
            print("Pattern doesn't exist...")
            return None
        if self.__user_list.count(a) > 1 and self.__confirm(mode=Data.EDIT):
            value_index_positions = self.__get_index_positions(value=a)
            for index in value_index_positions:
                self.__user_list[index] = b
            return value_index_positions
        # Will complete if only one value in stack or User don't confirm
        self.__user_list[self.__user_list.index(a)] = b
        return b

    def delete(self, number: int) -> list or None:
        """Remove from the stack all repetitions of the number"""
        if not number in self.__user_list:
            print("The number does not exist in the list")
            return None
        if number in self.__user_list and self.__confirm(mode=Data.DELETE):
            value_index_positions = self.__get_index_positions(value=number)
            for index in reversed(value_index_positions):
                del self.__user_list[index]
            return value_index_positions
        
    def find(self, number: int) -> int or None:
        """Find the number in stack. Returns the index."""
        if not number in self.__user_list:
            print("The number does not exist in the list")
            return None
        return self.__user_list.index(number)

    def __str__(self) -> str:
        """Returns the representation of the object"""
        if self.__confirm(mode=Data.SHOW):
            return f"List: {self.__user_list[::-1]}"
        return f"List: {self.__user_list}"


if __name__ == "__main__":
    print("This module for import not for execute!")