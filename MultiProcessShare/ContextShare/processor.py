"""
Mock any module configuration
"""
import sys
from multiprocessing.managers import SyncManager


class Namespace():
    pass

def _inject(pseq, *args, **kwargs):
    print("Calling the hidden meme function %s with \n%s\n%s" %
          (pseq, args, kwargs))
    _mgr = _WrapManager(address=("0.0.0.0", 50000), authkey=b"aigis")
    _mgr.connect()
    tclass = _mgr.process()
    return tclass.get_the_stuff(pseq, *args, **kwargs)
    #return _mgr.returndict().pop("return")

class cool():
    def __init__(self):
        self.pseq = []

    def __call__(self, *args, **kwargs):
        return _inject(self.pseq, *args, **kwargs)

    def __getattr__(self, attr):
        self.pseq.append(attr)
        return self


class wrapper():
    def __getattr__(self, attr):
        return cool().__getattr__(attr)


class _WrapManager(SyncManager):
    pass
_WrapManager.register("process")
_WrapManager.register("returndict")


sys.modules["processor"] = wrapper()
