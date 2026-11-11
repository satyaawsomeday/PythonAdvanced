#Constructors
class MyClass:

   #class variables
   var1 = "Satya"
   var2 = "Narayana"

   #instance variables
   def __init__(self,dyn1,dyn2, dyn3):
      self.dyn1 = dyn1 #pulblic variable
      self.__dyn2 = dyn2 #private variable
      self._dyn3 = dyn3 #protected variable

   def func1(self):
      print(f"Hello World, {self.dyn1}")

   def func2(self):
      print(f"Hello Python, {self.__dyn2}")

   def func3(self):
      print(f"Hello Java, {self._dyn3}") 

obj= MyClass("Abc", "Narayana", "Java")
print(obj.dyn1)
print(obj._dyn3) #protected variable can be accessed outside the class but it is not recommended

