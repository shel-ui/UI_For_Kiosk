class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil", 25)
p2 = Person("Jack", 23)

p1.greet()


class Car:
    def __init__(self, size, color):
        self.size = size
        self.color = color

    def runnin(self):
        print("This Car wheel size is " + self.size)