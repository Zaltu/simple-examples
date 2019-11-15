"""
Mock any module configuration
"""
import sys
from multiprocess.managers import SyncManager


class _WrapManager(SyncManager):
    """
    Simple wrapper around SyncManager for cleanliness because classmethods
    """
# Register the pseq processing function
_WrapManager.register("process")
_WMGR = _WrapManager(address=("0.0.0.0", 50000), authkey=b"aigis")
_WMGR.connect()

def _inject(pseq, *args, **kwargs):
    """
    Underlying RPC logic powering the transfer. Connect to the RPC port and fetch the remote processor proxy,
    then pass it the pseq. It will return the result of the pseq processing. Almost all types are supported
    here thanks to relying on dill instead of cPickle.

    :param list pseq: the point sequence to call
    :param args: the args to pass to the pseq
    :param kwargs: the kwargs to pass to the pseq

    :returns: whatever the remote processing of the pseq returns, if it is a valid type
    :rtype: object
    """
    print("Calling the hidden meme function %s with \n%s\n%s" %
          (pseq, args, kwargs))
    tclass = _WMGR.process()
    return tclass.get_the_stuff(pseq, *args, **kwargs)

class CopyCat():
    """
    Copycat class structure that can be called on any pseq.
    Unfortunately requires a call to do anything, since there's no real way of knowing when the last element
    of the pseq is getting added.
    """
    def __init__(self):
        self.pseq = []

    def __call__(self, *args, **kwargs):
        """
        Denotes that a point in the pseq is getting called, so it runs the injection, ultimately forming an
        RPC call to the server with the current pseq.

        :param args: args to pass to the server
        :param kwargs: kwargs to pass to the server

        :returns: the return of the injected call from the server
        :rtype: object
        """
        return _inject(self.pseq, *args, **kwargs)

    def __getattr__(self, attr):
        """
        Allows the copycat class to store the full requested pseq when receiving a call. In reality, calling
        a pseq on the copycat only ever returns itself, it simply logs that a string attribute was requested
        so the info can be passed on when it is eventually called.

        :param str attr: the attribute requested

        :returns: self, the current copycat object
        :rtype: CopyCat
        """
        self.pseq.append(attr)
        return self


class Wrapper():
    """
    Wrapper class around the CopyCat namespace to ensure that each call's pseqs don't get mixed up.
    """
    def __getattr__(self, attr):
        """
        Override of getattr to generate a copy of CopyCat to be used to generate this call's pseq.

        :param str attr: starting point's seq

        :returns: the CopyCat object at the correct pseq for further processing
        :rtype: CopyCat
        """
        return CopyCat().__getattr__(attr)


# Syntaxical sugar. Set the processor to the wrapper directly on import.
sys.modules["processor"] = Wrapper()
