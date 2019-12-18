"""
Multiprocessing context share, but with dill instead of pickle/cPickle
_processor represents the abstract, serverside code that holds the actual code to run in practice.
"""
#pylint: disable=invalid-name,attribute-defined-outside-init
from multiprocess.managers import SyncManager

OUTOFSCOPE = "unlucky dude"

class MuhContainer():
    """
    Sample complex object to return via RPC/Serialization
    """
    def __init__(self):
        self.text = "Hit or miss, I guess they never miss, huh?"
    def prove(self):
        """
        Sample complex operation to be callable from RPC
        """
        print(self.text)
    def move(self):
        print(OUTOFSCOPE)

# Create a local sample object for testing
M = MuhContainer()

def dreamsF():
    """
    Sample function to update a value locally and also return something simple.

    :returns: sample text
    :rtype: str
    """
    M.text = "You got a boyfriend I bet he doesn't kiss ya!"
    mainc.other = "He gon find another girl and he won't miss ya!"
    return "Change confirmed"

def clanF():
    """
    Sample function to return a complex object that should be maintained between processes via serialization
    and that can be updated in the parent process's runtime.

    :returns: a complex object, mutable in the parent process
    :rtype: MuhContainer
    """
    return M


class Namespace():
    """Empty placeholder class"""

# Build the sample complex namespace that could exist in a real application
memes = Namespace()
memes.nd = Namespace()
memes.nd.dreams = dreamsF
memes.nd.NAME = "MAD"

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

# Serve the manager
if __name__ == "__main__":
    wm = WrapManager(address=("0.0.0.0", 50000), authkey=b"aigis")
    print("Serving server\n")
    wm.get_server().serve_forever()
