from abc import ABC, abstractmethod


class Employee(ABC):

  @abstractmethod
  def work(self):
    pass

  @abstractmethod
  def get_salary(self):
    pass


class Developer(Employee):

  def work(self):
    print("Developer is writing code.")

  def get_salary(self):
    return 30000



class Teacher(Employee):

  def work(self):
    print("Teacher is teaching.")

  def get_salary(self):
    return 25000


if __name__ == "__main__":
  print("=== Employee Management System ===")

  dev = Developer()
  dev.work()
  print(f"Salary: {dev.get_salary():,}\n")

  teacher = Teacher()
  teacher.work()
  print(f"Salary: {teacher.get_salary():,}")