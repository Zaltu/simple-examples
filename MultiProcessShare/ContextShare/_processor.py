#pylint: disable=invalid-name,attribute-defined-outside-init
from multiprocessing.managers import SyncManager, NamespaceProxy
from multiprocessing import Manager

D = Manager().dict()

def dreamsF(*args, **kwargs):
    return "they say dreamers never die"

def clanF(*args, **kwargs):
    return "{\"noice\":\"inb4 Sept finds out\"}"


class Namespace():
    pass

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
    def get_the_stuff(self, pseq, *args, **kwargs):
        """
        Endpoint to call any value found in mainc, forwarding the parameters used.

        :param list[str] pseq: point sequence in mainc to follow
        :param args: args to forward
        :param kwargs: kwargs to forward

        :returns: result of final layer
        :rtype: object
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
    pass
WrapManager.register("process", callable=parse_pseq)
WrapManager.register("returndict", callable=lambda: D)


if __name__ == "__main__":
    wm = WrapManager(address=("0.0.0.0", 50000), authkey=b"aigis")
    print("Serving server\n")
    wm.get_server().serve_forever()
