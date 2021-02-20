import json

class Human():
    def __init__(self, age, name, surname):
        self.age = age
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"Human:{self.name}{self.surname}{self.age}"
    def convert_to_dict(self):
        return self.__dict__




# def json_to_file(humans:list):
#     for human in humans
#         human._dict = human.convert_to_dict()
#         human._json = json.dump()
#     ]
#
#     try:
#         with open("./training.json", "w") as fd:
#             json.dump(json_list, fd, indent=2)
#     except (IOError, Exception) as e:
#         print(f'Problem with writing to file, more info: {e.args}')