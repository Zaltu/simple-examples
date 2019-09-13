"""
Import values from one runtime namespace to another
"""
import setall
import inspect


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
class Namespace():
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


    def __repr__(self):
        keys = sorted(self.__dict__)
        items = ("{}={!r}".format(k, self.__dict__[k]) for k in keys)
        return "{}({})".format(type(self).__name__, ", ".join(items))


    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class ViaDict():
    """
    Define a holder class and create functions to append to it's namespace.
    Ultimately functions very similarly to inheretance.
    """
    def __init__(self):
        self.coolvalue = "i got this"

    def joindict(self, mod):
        """
        Join a given dict with this class' dict, essentially extending the functionality of the class.

        :param module mod: module who's functionality to port
        """
        for name in mod.ALL:
            pseq = name.split(".")
            leafdict = self._recurdict(mod, pseq, 0)
            setattr(self, pseq[0], leafdict)

    def _recurdict(self, mod, pseq, i):
        if i == len(pseq):
            return mod
        print(pseq)
        print(pseq[i])
        if pseq[i] in mod.__dict__:
            return self._recurdict(mod.__dict__[pseq[i]], pseq, i+1)
        elif pseq[i] in dir(mod):
            ns = Namespace()
            ns.__dict__[pseq[i]] = getattr(mod, pseq[i])
            return ns

    def showdict(self):
        """
        Convenience function, print the dict
        """
        import pprint
        pprint.pprint(self.__dict__)


# Innitialize the holder class
V = ViaDict()
# Join the dict of all callable values (class and func) of the imported setall module
V.joindict(setall)
V.showdict()
# Class now has the functionality of the imported values.
# Notice that there needs to be a "None" value passed here, since the function itself
# expects a "self" value, which is necessary when importing into the locals namespace
# from the previous example, but not here.
V.acoolfunc(None, "hewwo? - class")
V.ACoolClass()
V.a.betterprint()
V.pprint.pprint("layered pprint")



# Third test
def addmodule(mod):
    """
    Add all callable values from a given module's globals to this module's globals.

    :param module mod: module to import
    """
    for name, cls in dict([(name, cls) for name, cls in mod.__dict__.items() if name in mod.ALL]).items():
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
