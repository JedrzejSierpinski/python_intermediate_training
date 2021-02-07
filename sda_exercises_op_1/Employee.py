from datetime import date

from python_intermidiate_training.sda_exercises_op_1.Person import Person


class Employee(Person):

    def __init__(self, salary, name: str, surname: str, birthday: date, salary=1000.0):
        super().__init__(name, surname, birthday):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @staticmethod
    def get_employee_birthday(birthday: date):
        employee_birthday = 0

    def employee_birthday(birthday: date) -> bool:
        return
