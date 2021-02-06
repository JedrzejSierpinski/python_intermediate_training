# from python_intermidiate_training.sda_exercises_op_1.cat import Cat
# from python_intermidiate_training.sda_exercises_op_1.dog import Dog
from python_intermidiate_training.sda_exercises_op_1.Object_Class import *


#
# def main():
#     cat_object = Cat("Filemon")
#     cat_object_2 = Cat("Mruczek", "miałmiał")
#     cat_object_3 = Cat("Pipak")
#     cat_object_4 = Cat("Jarosław")
#     dog_object = Dog("Burek", "Hauhau")
#
#
#
#     cats = [cat_object, cat_object_2, cat_object_3, cat_object_4]
#     animals = []
#     animals.append(cat_object)
#     animals.append(cat_object_2)
#     animals.append(cat_object_3)
#     animals.append(cat_object_4)
#     animals.append(dog_object)
#
#
#     for animal in animals:
#         sound = animal.make_sound()
#         print(sound)
#
#     cat_object.eat_mouse()
#     cat_object.eat_mouse()
#     cat_object.eat_mouse()
#
#     print("Teraz będzie żarł drugi kot")
#
#     cat_object_2.eat_mouse()
#
# zmienna sound jest stringiem

def main():
    circle1 = Circle(5)
    circle2 = Circle(12)
    circle3 = Circle(12)
    triandgle1 = Triangle(7, 3)
    triandgle2 = Triangle(10, 8)
    triandgle3 = Triangle(5, 12)
    rectangle1 = Rectangle(4, 8)
    rectangle2 = Rectangle(14, 25)
    rectangle3 = Rectangle(10, 2)

    print(circle1.getArea())
    print(triandgle1.getArea())
    print(rectangle1.getArea())


if __name__ == "__main__":
    main()
#
