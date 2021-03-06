"""
_processor represents the abstract, serverside code that holds the actual code to run in practice.
"""
#pylint: disable=invalid-name,attribute-defined-outside-init,unused-argument
from multiprocessing.managers import SyncManager

def dreamsF(*args, **kwargs):
    """
    Sample function 1. Returns simple data.

    :param args: args received
    :param kwargs: kwargs received

    :returns: sample text
    :rtype: str
    """
    return "they say dreamers never die"

def clanF(*args, **kwargs):
    """
    Sample function 2. Returns simple data.

    :param args: args received
    :param kwargs: kwargs received

    :returns: sample text
    :rtype: dict
    """
    return {"noice":"inb4 Sept finds out"}


class Namespace():
    """Empty placeholder class"""

# Build the sample complex namespace that could exist in a real application
memes = Namespace()
memes.nd = Namespace()
memes.nd.dreams = dreamsF

the = Namespace()
the.oc = Namespace()
the.oc.clan = clanF

mainc = Namespace()
mainc.memes = memes
mainc.the = the


class parse_pseq():
    """
    Wrapper class around the logic used to parse the pseq of the requested call.
    A class instance is required by the multiprocessing manager library.
    """
    def get_the_stuff(self, pseq, *args, **kwargs):
        """
        Endpoint to call any value found in mainc, forwarding the parameters used.

        :param list[str] pseq: point sequence in mainc to follow
        :param args: args to forward
        :param kwargs: kwargs to forward

        :returns: result of final layer
        :rtype: object

        :raises Exception: if the arguments do not match the requested function's signature.
        """
        print("Remote processing\nmainc.%s\nargs: %s\nkwargs: %s\n\n" % (".".join(pseq), args, kwargs))
        toret = self._recurpseq(pseq, 0, mainc)
        if callable(toret):
            toret = toret(*args, **kwargs)
        elif args or kwargs:
            raise Exception("Too many arguments:\n%s\n%s" % (args, kwargs))
        return toret


    def _recurpseq(self, pseq, i, mod):
        """
        Recursively parse the mod until the end of the point sequence

        :param list[str] pseq: the point sequence
        :param int i: current index
        :param object mod: object on this layer

        :returns: object at the final layer of the point sequence
        :rtype: object
        """
        if i+1 == len(pseq):
            return getattr(mod, pseq[i])
        return self._recurpseq(pseq, i+1, getattr(mod, pseq[i]))


class WrapManager(SyncManager):
    """Wrapper around the multiprocessing manager because classmethods."""
# Register our pseq parsing wrapper class
WrapManager.register("process", callable=parse_pseq)

# Serve the manager.
if __name__ == "__main__":
    wm = WrapManager(address=("0.0.0.0", 50000), authkey=b"aigis")
    print("Serving server\n")
    wm.get_server().serve_forever()
