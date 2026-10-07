from abc import ABC, abstractmethod


class Animal(ABC):

  @abstractmethod
  def sound(self):
    pass


class Dog(Animal):

  def sound(self):
    print("Dog says: Woof!")

class Cat(Animal):

  def sound(self):
    print("Cat says: Meow!")


if __name__ == "__main__":
  print("=== Animal Sound System ===")

  my_dog = Dog()
  my_dog.sound()

  my_cat = Cat()
  my_cat.sound()