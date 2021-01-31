from python_intermidiate_training.sda_exercises_op_1.cat import Cat


def main():
    cat_object = Cat("Filemon")
    cat_object_2 = Cat("Mruczek", "miałmiał")
    cat_object_3 = Cat("Pipak")
    cat_object_4 = Cat("Jarosław")

    # cats = [cat_object, cat_object_2, cat_object_3, cat_object_4]
    cats = []
    cats.append(cat_object)
    cats.append(cat_object_2)
    cats.append(cat_object_3)
    cats.append(cat_object_4)

    # for cat in cats:
    #     sound = cat.make_sound()
    #     print(sound)

    cat_object.eat_mouse()
    cat_object.eat_mouse()
    cat_object.eat_mouse()

    print("Teraz będzie żarł drugi kot")

    cat_object_2.eat_mouse()

# zmienna sound jest stringiem

if __name__ == "__main__":
    main()

