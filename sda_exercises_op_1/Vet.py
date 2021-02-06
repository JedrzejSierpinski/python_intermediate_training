from python_intermidiate_training.sda_exercises_op_1.Animal import Animal
from python_intermidiate_training.sda_exercises_op_1.cat import Cat
from python_intermidiate_training.sda_exercises_op_1.dog import Dog


class Vet:

    @staticmethod
    def sayCatHello(cat: Cat):
        print(f'Witaj {cat.name}')

    @staticmethod
    def sayDogHello(dog: Dog):
        print(f'Witaj {dog.name}')

    @staticmethod
    def sayHello(animal: Animal):
        print(f'Witaj {animal.name}')
