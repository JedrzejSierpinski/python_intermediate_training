import pickle

import fd as fd


def pickle_write(items: list):
    try:
        with open('./data.pickle', 'wb') as fd:
            pickle.dump(items, fd)
            pickle.dumps(items, fd)
    except (IOError, Exception) as e:
        print(f'Exception while writing pickle format info: {e.args}')
    print(f'Pickle write finish')

def pickle_read(items: list):
    string_list = []
    try:
        with open('./data.pickle', 'wb') as fd:
            pickle.dump(items, fd)
            pickle.dumps(items, fd)
    except (IOError, Exception) as e:
        print(f'Exception while writing pickle format info: {e.args}')


def main():
    abc = ['bread', 'butter', 'cola']
    pickle_write(abc)
    list_of_strings = pickle_read()
    print(list_of_strings)


if __name__ == "__main__":
    main()
