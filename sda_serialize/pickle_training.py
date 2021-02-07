import pickle

import fd as fd


def pickle_write(items: list):
    try:
        with open('./data.pickle', 'wb') as fd:
            pickle.dump(items, fd)
            pickle.dumps(items, fd)
    except (IOError, Exception) as e:
        print(f'Exception while writing pickle format info: {e.args}')
