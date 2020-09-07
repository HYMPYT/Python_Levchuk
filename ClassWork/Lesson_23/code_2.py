class A:
    def __init__(self, val):
        self.field_1 = val
    
    def __setattr__(self, name, value):
        if name == 'field_1':
            self.__dict__[name] = value
        else:
            raise AttributeError