from abc import abstractmethod, ABC

class Movable(ABC):
    pass

class Car(Movable):

    @abstractmethod
    def move(self) -> str:
        return f'Jadę'



