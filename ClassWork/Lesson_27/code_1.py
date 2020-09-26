from typing import Any

class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, value: Any) -> None:
        self.__stack.append(value)

    def pop(self) -> Any:
        if len(self.__stack) > 0:
            val = self.__stack[-1]
            del self.__stack[-1]
            return val

    def __str__(self):
        return f"{self.__stack}"

class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def push(self, value: Any) -> None:
        Stack.push(self, value)
        self.__sum += value

    def pop(self) -> Any:
        val = Stack.pop(self)
        if val:
            self.__sum -= val
        return val

    @property
    def sum(self) -> int:
        return self.__sum
        


if __name__ == "__main__":
    stack = AddingStack()

    for i in range(5):
        stack.push(i)

    print(stack.sum)

    for i in range(5):
        print(stack.pop(), end=" ")