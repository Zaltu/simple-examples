"""
Import values from one runtime namespace to another
"""
import setall



# First test
class MyHolder():
    """
    Holder class containing all the values designated in the imported module's `assign` function.
    Not that setall.assign will not work if called within a function since locals becomes a proxy
    at that point.
    """
    setall.assign(locals())

# Initialize holder class, calling the import of setall's values.
H = MyHolder()
# Call one of the functions defined in setall via the holder class.
H.acoolfunc("hewwo? - locals")
# Initialize a class, defined like a subclass from the module import
H.ACoolClass()



# Second test
class ViaDict():
    """
    Define a holder class and create functions to append to it's namespace.
    Ultimately functions very similarly to inheretance.
    """
    def joindict(self, toadd):
        """
        Join a given dict with this class' dict, essentially extending the functionality of the class.

        :param module toadd: module who's functionality to port
        """
        toadd = dict([(name, cls) for name, cls in setall.__dict__.items() if name in setall.__all__])
        self.__dict__.update(toadd)

    def showdict(self):
        """
        Convenience function, print the dict
        """
        print(self.__dict__)

# Innitialize the holder class
V = ViaDict()
# Join the dict of all callable values (class and func) of the imported setall module
V.joindict(setall)
# Class now has the functionality of the imported values.
# Notice that there needs to be a "None" value passed here, since the function itself
# expects a "self" value, which is necessary when importing into the locals namespace
# from the previous example, but not here.
V.acoolfunc(None, "hewwo? - class")
V.ACoolClass()
V.pprint.pprint("layered pprint")



# Third test
def addmodule(mod):
    """
    Add all callable values from a given module's globals to this module's globals.

    :param module mod: module to import
    """
    for name, cls in dict([(name, cls) for name, cls in mod.__dict__.items() if name in mod.__all__]).items():
        globals()[name] = cls

# Add setall's module to this one
addmodule(setall)
# Pylint will scream that these values are not defined, but they have been imported on
# runtime into getall's globals
# pylint: disable=undefined-variable
acoolfunc(None, "hewwo? - module")
ACoolClass()
pprint.pprint(dir())
# pylint: enable=undefined-variable
