class StringStack:
    """This class implements a stack of strings. The stack has a fixed size."""
    SIZE = 15

    def __init__(self):
        self.__stack = [] 

# * Service method
# * ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __message(self, mod, flag = True) -> str:
        """Messages for methods in the object"""
        if mod == 'push':
            return "Successful operation" if flag else "Error: size over"
        
        if mod == 'pop':
            return "Successful operation" if flag else "Error: items do not exist"

        if mod == 'clear':
            return "Successful operation"

        if mod == 'get':
            return "Successful operation" if flag else f"You must use index from 0 to {StringStack.SIZE} or from -1 to -{StringStack.SIZE + 1}"

# * Common methods
# * ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def push(self, string: str) -> str:
        """Adding the element into stack. Returns the message."""
        if len(self.__stack) < StringStack.SIZE:
            self.__stack.append(string)
            return self.__message('push')
        return self.__message('push', flag=False)

    def pop(self) -> tuple:
        """Remove last element from stack.
        Returns the tuple(a, b) where a: removed value b: message."""
        if len(self.__stack) > 0:
            result = self.__stack[-1]
            del self.__stack[-1]
            return result, self.__message('pop')
        return None, self.__message('pop', flag=False)

    def is_empty(self) -> bool:
        """Checks if the stack is empty."""
        return True if len(self.__stack) == 0 else False

    def is_full(self) -> bool:
        """Checks if the stack is full."""
        return True if len(self.__stack) == StringStack.SIZE - 1 else False

    def clear(self) -> str:
        """Cleans all items in the stack"""
        self.__stack = []
        return self.__message('clear')

    def __getitem__(self, key: int) -> tuple:
        """Returns the tuple(a, b) where a: element on index b: message"""
        try:
            return self.__stack[key], self.__message('get')
        except IndexError:
            return None, self.__message('get', flag=False)

    def __len__(self) -> int:
        """Returns the amount of strings in the stack."""
        return len(self.__stack)


if __name__ == "__main__":
    print("This module for import not for execute!")