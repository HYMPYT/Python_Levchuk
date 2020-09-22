class MyClass(object):
    pass

MyClass2 = type('MyClass2', (), {})

print(MyClass)
print(MyClass2)


# def choose_class(name):
#     if name == 'foo':
#         class Foo:
#             pass
#         return Foo
#     else:
#         class Bar:
#             pass
#         return Bar

# MyClass = choose_class('foo')
# print(MyClass)


# def make_hook(f):
#     """Декоратор для включення 'foo' метода в __foo__"""
#     f.is_hook = 1
#     return f

# class MyType(type):
#     def __new__(cls, name, bases, attrs):
#         if name.startswith('None'):
#             return None

#         newattrs = {}
#         for attrname, attrval in attrs.items():
#             if getattr(attrval, 'is_hook', 0):
#                 newattrs["__%s__" % attrname] = attrval
#             else:
#                 newattrs[attrname] = attrval
#         return super(MyType, cls).__new__(cls, name, bases, newattrs)

#     def __init__(self, name, bases, attrs):
#         super(MyType, self).__init__(name, bases, attrs)
#         print(f"Хочу зареєструвати клас {self}")

#     def __add__(self, other):
#         class AutoClass(self, other):
#             pass
#         return AutoClass

#     def unregister(self):
#         print(f"Хочу зняти реєстрацію класу {self}")

# class MyObject:
#     __metaclass__ = MyType

# class NoSample(MyObject):
#     pass


# class Example(MyObject):
#     def __init__(self, value):
#         self.value = value

#     @make_hook
#     def add(self, other):
#         return self.__class__(self.value, other.value)

# if __name__ == "__main__":
#     Example.unregister()
#     ex = Example(10)