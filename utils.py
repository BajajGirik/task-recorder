import datetime

def get_timestamp():
    return datetime.datetime.now().timestamp()


def print_separator():
    print("**********************")


def print_header(*args):
    print("")
    print_separator()
    print(*args)
    print("")
    print_separator()