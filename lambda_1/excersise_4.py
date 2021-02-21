from random import randint
#lista składana
def excersise_4():
    random_list = [randint(0, 101) for item in range(10)]
    print("Before")
    print(random_list)
    print("After")
    print(list(map(lambda number: number * 2, random_list)))