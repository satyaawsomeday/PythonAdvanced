#Constructors
class MyClass:

   #class variables
   var1 = "Satya"
   var2 = "Narayana"

   #instance variables
   def __init__(self,dyn1,dyn2, dyn3):
      self.var1 = dyn1 #pulblic variable
      self.var2 = dyn2 #pulblic variable
      self.var3 = dyn3

   def func1(self):
      print(f"Hello World, {self.var1}")

   def func2(self):
      print(f"Hello Python, {self.var2}")

   def func3(self):
      print(f"Hello Java, {self.var3}")

obj= MyClass("Satya", "Narayana", "Java")
obj.func1()
obj.func2()
obj.func3()
MyClass.func1(obj)