from python_intermidiate_training.sda_exercises_op_1.Animal import Animal
from python_intermidiate_training.sda_exercises_op_1.Movable import Movable


class Cat(Movable, Animal):

    def __init__(self, name: str, sound='meow', eaten_mouse=0):
        self.name = name
        self.sound = sound
        self.eaten_mouse = eaten_mouse

    def eat_mouse(self) -> int:
        self.eaten_mouse += 1
        print (f'zjadłem {self.eaten_mouse} myszy')
        return self.eaten_mouse

    def make_sound(self) -> str:
        return f'Name is {self.name} sound is {self.sound}'


