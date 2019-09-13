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
