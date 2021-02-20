# def main():
#     a, b = print_hello_world(1, 2)
#     print(f'In main: {a} {b}')
# from decorators.case_2 import read_file
from python_intermidiate_training.sda_exercises_op_1.decorators.case2 import read_file


def main():
    read_file(file_path='./abc')
#     a, b = print_hello_world(1, 2)
#     print(f'In main: {a} {b}')
#
#
# def wrap_before_and_after(func):
#     def wrapper(*args, **kwargs):
#         print('Before')
#         result = func(*args, **kwargs)
#         print('After')
#         return result
#     return wrapper

def wrap_before_and_after(func):
    def wrapper(*args, **kwargs):
        print('Before')
        result = func(*args, **kwargs)
        print('After')
        return result
    return wrapper



@wrap_before_and_after
def print_hello_world(a, b):
    print("Hello world!")
    print(f'{a, b}')
    return a, b
# @wrap_before_and_after
# def print_hello_world(a, b):
#     print("Hello world!")
#     print(f'{a, b}')
#     return a, b


if __name__ == '__main__':
    main()