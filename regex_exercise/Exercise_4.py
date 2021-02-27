import re


def regex_ex_3():
    print("Write login")

    value = input()

    expression = r"[a-zA-Z0-9_\-]{8,16}"
    if re.fullmatch(expression, value):
        print("This is correct login")
    else:
        print("This login is incorrect, please try again")


def regex_ex_4():
    print("Write smt with ala")

    value = input()

    expression = r".*ala.*"
    if re.fullmatch(expression, value):
        print("Found ala")
    else:
        print("Not found ala")
