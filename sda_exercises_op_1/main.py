from python_intermidiate_training.sda_exercises_op_1.cat import Cat


def main():
    cat_object = Cat("Filemon")
    sound = cat_object.make_sound()
    print(sound)

# zmienna sound jest stringiem


if __name__ == "__main__":
    main()
