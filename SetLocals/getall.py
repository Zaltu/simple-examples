"""
Import the values of another module into the class namespace
"""
import setall


class MyHolder():
    """
    Holder class containing all the values designated in the imported module's `assign` function.
    """
    setall.assign(locals())


# Initialize holder class, calling the import of setall's values.
H = MyHolder()

# Call one of the functions defined in setall via the holder class.
H.acoolfunc("hewwo?")

# Create a class, defined like a subclass from the module import
L = H.ACoolClass()
