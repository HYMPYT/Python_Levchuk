class Foo:
    class_attr = "I'm a class attribute"

    def __init__(self):
        self.dict_attr = "I'm in a dict!!!"

    @property
    def property_attribute(self):
        return "I'm a read-only property"

    def __getattr__(self, item):
        return "I'm dynamically returned!"
    
    def my_get_attribute(self, item):
        if item in self.__class__.__dict__:
            print("Retrieving from self.__class__.__dict__")
            v = self.__class__.__dict__[item]
        elif item in self.__dict__:
            print("Retrieving from self.__dict__")
            v = self.__dict__[item]
        else:
            print("Retrieving from self.__getattr__")
            v = self.__getattr__(item)
        return v



foo = Foo()
print(foo.class_attr)
print(foo.dict_attr)
print(foo.property_attribute)
print(foo.assadsadsadas)
print()
print(foo.my_get_attribute("class_attr"))
print(foo.my_get_attribute("dict_attr"))
print(foo.my_get_attribute("property_attribute"))
print(foo.my_get_attribute("assadsadsadas"))