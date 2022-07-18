#!/usr/bin/python3
<<<<<<< HEAD

def safe_print_integer(value):

    try:

        print("{:d}".format(value))

    except (ValueError, TypeError):

        return False

    else:

=======
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return False
    else:
>>>>>>> b6b7632418c145a2089ffdbbcf849ad656ef1681
        return True
