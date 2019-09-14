"""
Import values from one runtime namespace to another
"""
import setall

# Second test
class Namespace():
    def __repr__(self):
        keys = sorted(self.__dict__)
        items = ("{}={!r}".format(k, self.__dict__[k]) for k in keys)
        return "{}({})".format(type(self).__name__, ", ".join(items))

class ViaDict():
    """
    Define a holder class and create functions to append to it's namespace.
    Ultimately functions very similarly to inheretance.
    """
    def joindict(self, mod):
        """
        Join a given dict with this class' dict, essentially extending the functionality of the class.

        :param module mod: module who's functionality to port
        """
        for name in mod.ALL:
            pseq = name.split(".")
            print("\nRunning for %s" % name)
            if hasattr(self, pseq[0]):
                print("Reusing namespace %s\n%s" % (pseq[0], getattr(self, pseq[0])))
                leafdict = self._recurdict(getattr(mod, pseq[0]), pseq, 1, ns=getattr(self, pseq[0]))
            elif len(pseq) > 1:
                leafdict = Namespace()
                self._recurdict(getattr(mod, pseq[0]), pseq, 1, leafdict)
            else:
                leafdict = getattr(mod, name)
            setattr(self, pseq[0], leafdict)

    def _recurdict(self, mod, pseq, i, ns):
        if i+1 == len(pseq):
            print("Returning mod %s" % getattr(mod, pseq[i]))
            print("Current given ns is\n%s" % ns)
            setattr(ns, pseq[i], getattr(mod, pseq[i]))
            return
        if pseq[i] in dir(mod):
            if pseq[i] in dir(ns):
                print("Reusing namespace %s\n%s" % (pseq[i], getattr(ns, pseq[i])))
                self._recurdict(getattr(mod, pseq[i]), pseq, i+1, getattr(ns, pseq[i]))
            else:
                print("Generating new NS for %s in ns\n%s" % (pseq[i], ns))
                setattr(ns, pseq[i], Namespace())
                self._recurdict(getattr(mod, pseq[i]), pseq, i+1, getattr(ns, pseq[i]))
            print("Returning ns %s" % ns)
            return ns
        raise Exception("Cannot find %s in %s" % (pseq[i], dir(mod)))

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
print("\n\nPrinting class dict:")
V.showdict()

print("\n\nPrinting tests:")
# Class now has the functionality of the imported values.
# Notice that there needs to be a "None" value passed here, since the function itself
# expects a "self" value, which is necessary when importing into the locals namespace
# from the previous example, but not here.
V.a.betterprint()
V.a.ruhoh.pprint("big brain")
#print(V.a.coolvalue)  # Should crash

V.acoolfunc(None, "hewwo? - class")
V.ACoolClass()
V.pprint.pprint("layered pprint")


