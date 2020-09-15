class SortKey:
    """This class is functor"""
    def __init__(self, attr: str):
        self.attr = attr

    def __call__(self, other):
        return getattr(other, self.attr)


if __name__ == "__main__":
    print("This module for import not for execute")