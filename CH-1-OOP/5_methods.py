class MyClass:
    my_var=100

    def __init__(self):
        print("this is a constructor method")

    def __str__(self):
        return "this is a dunder method"
    
    @classmethod
    def _change_value(cls, new_value):#protected class method
        cls.my_var = new_value

    @staticmethod
    def dummy():
        print("This is a dummy method")

# obj = MyClass()
# print(obj.my_var)  # Output: 100
# obj._change_value(200)
# print(obj.my_var)
# obj2 = MyClass()
# print(obj2.my_var)  # Output: 100
# obj3=MyClass()
# print(obj3.dummy())
obj4=MyClass()
print(obj4)
