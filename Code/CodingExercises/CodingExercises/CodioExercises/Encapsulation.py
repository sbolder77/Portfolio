class Phone:
  def __init__(self, model, storage, megapixels, carrier):
    self._model = model
    self._storage = storage
    self._megapixels = megapixels
    self._carrier = carrier

class PrivateClass:
  def __init__(self):
    self.__private_attribute = "I am a private attribute"
    
  def __private_method(self):
    return "I am a private method"
  
  def helper_method(self):
    return self.__private_method()

class PrivateClass1:
  def __init__(self):
    self.__private_attribute = "I am a private attribute"
    
obj = PrivateClass()
print(obj.helper_method())

obj = PrivateClass1()
print(obj._PrivateClass__private_attribute)
    
my_phone = Phone("iPhone", 256, 12, "AT&T")
print(my_phone.make)
print(my_phone.storage)
my_phone.storage = 64
print(my_phone.megapixels)
print(my_phone.__dict__)

class TestClass:
  def __init__(self, num1, num2):
    self._num1 = num1
    self._num2 = num2
    self._sum = 0
    
  def get_num1(self):
    return self._num1
  
  def set_num1(self, new_value):
    self._num1 = new_value
    
  def get_num2(self):
    return self._num2
  
  def set_num2(self, new_value):
    self._num2 = new_value
    
  def get_sum(self):
    return self._sum
  
  def set_sum(self, new_value):
    self._sum = new_value

  @property
  def sum(self):
      return self._num1 + self._num2

obj = TestClass(5, 7)
print(obj.get_num1())
print(obj.get_num2())
#obj.set_sum(obj.get_num1() + obj.get_num2())
#obj.sum(obj.num1 + obj.num2)
print(obj.sum)

class Person:
  def __init__(self, name, age):
    self._name = name
    self._age = age
  
  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, new_name):
    if type(new_name) != str:
      raise TypeError("Names must be expressed as a string")
    self._name = new_name
    
  @property
  def age(self):
    return self._age
  
  @age.setter
  def age(self, new_age):
    if new_age < 0:
      raise ValueError("Age must be a positive number.")
    self._age = new_age
  
c = Person("Calvin", "6")
print(c.name)
print(c.age)
c.age = -17
c.name = "False"
print(c.name)
print(c.age)

#class TestClass:
#  def __init__(self):
#    self._private = "I am private"
    
#    @private.setter
#    def private(self, new_value):
#      self._private = new_value

#  @property
#  def private(self):
#    return self._private

#class Person:
#  def __init__(self, name, age):
#    self._name = name
#    self._age = age
  
#  def get_name(self):
#    return self._name
  
#  def set_name(self, new_name):
#    self._name = new_name
  
#  def get_age(self):
#    return self._age
  
#  def set_age(self, new_age):
#    self._age = new_age
  
#  name = property(get_name, set_name)
#  age = property(get_age, set_age)
  
#c = Person("Calvin", 6)
#print(c.name)
#print(c.age)
#c.name = "Hobbes"
#c.age = 8
#print(c.name)
#print(c.age)

#@color.setter
#def color(self, new_color):
#    primary_colors = ["red", "blue", "yellow"]
#        if new_color not in primary_colors:
#            raise ValueError("New color must be a primary color")
#        self.color = new_color