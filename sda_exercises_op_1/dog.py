from python_intermidiate_training.sda_exercises_op_1.Animal import Animal


class Dog(Animal):
    def __init__(self, name: str, sound: str):
        super().__init__()
        self.name = name
        self.sound = sound

    def make_sound(self) -> str:
        return f'Pies wydaje dźwięk {self.sound} i ma na imię {self.name}'




