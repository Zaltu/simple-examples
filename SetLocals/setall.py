"""
Define some COOL stuff and assign it to a given namespace.
"""

def acoolfunc(self, val):
    """
    Print val

    :param str val: printable value
    """
    print(val)


class ACoolClass():
    """
    Class test, prints a thing
    """
    def __init__(self):
        print("initializing class pepepog")


def assign(externals):
    """
    Assign functions and classes to a local value dictionary.
    The string assigned as key will be the callable in the namespace calling this function.
    Can only be used in module and class namespaces.

    :param NameSpace externals: the `locals()` value of the namespace importing these variables.
    """
    externals["acoolfunc"] = acoolfunc
    externals["ACoolClass"] = ACoolClass
