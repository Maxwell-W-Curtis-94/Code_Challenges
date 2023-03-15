# simple
class InformalInterface:
    def method_one(self, a: int, b: int, c: int) -> int:
        pass

    def method_two(self, *args) -> list:
        pass


class UsingInformalInterface(InformalInterface):
    def __init__(self):
        pass

    def method_one(self, a: int, b: int, c: int) -> int:
        pass

    def method_two(self, *args):
        pass


# Metta class

class MetaClass(type):
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))


class MetaInterface(metaclass=MetaClass):
    pass
