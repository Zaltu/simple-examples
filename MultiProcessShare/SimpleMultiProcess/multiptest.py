"""
Tests for sharing complex objects between python processes.

Note that the mutliprocessing.managers create proxies, not really "endpoints",
so variable changes will not propagate
"""
from multiprocessing import Process
from multiprocessing import Manager
from multiprocessing.managers import BaseManager
import subprocess
import os

from pprint import pprint as pp
from requests.exceptions import HTTPError

class MyClass():
    """
    Dummy class with a test function using an external import
    """
    value = HTTPError
    def niceprint(self):
        """
        Dummy function
        """
        pp({"pretty": self.value})

A = MyClass()


def dreamsF(*args, **kwargs):
    print(os.getpid())
    return "they say dreamers never die"

def clanF(*args, **kwargs):
    return "inb4 Sept finds out"

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


def themanager():
    """
    Manager container. Pops open the inter-process server and serves it until killed.

    :returns: manager with registered class
    :rtype: BaseManager
    """
    BaseManager.register('get_my_class', callable=lambda: A)
    mana = BaseManager(address=('', 50000), authkey=b'abracadabra')
    return mana


def multicalled(ns):
    """
    Meant to be called in a multiprocessing.Process for testing purposes.
    Connects to the managed queue from the original process and calls the stored value.

    :param SyncManager.Namespace ns: shared namespace
    """
    BaseManager.register('get_my_class')
    rpm = BaseManager(address=('', 50000), authkey=b'abracadabra')
    rpm.connect()
    rpclass = rpm.get_my_class()
    rpclass.niceprint()
    if ns:
        print("NS is set to %s" % ns)
        print(os.getpid())
        print(ns.memes.nd.dreams())


def test_multiprocess(ns=None):
    """
    Simplification of the steps to test mutliprocessing module connectivity

    :param SyncManager.Namespace ns: shared namespace
    """
    rp = Process(target=multicalled, args=(ns,))
    rp.start()
    rp.join()


def test_subprocess():
    """
    Simplification of the steps to test subprocessing module connectivity
    """
    p = subprocess.Popen(["python3.7", "multi2test.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()


if __name__ == "__main__":
    print("Launching Server process")
    mgr = themanager()
    SP = Process(target=mgr.get_server().serve_forever)
    SP.start()

    print("\nTesting multiprocess connect")
    test_multiprocess()

    print("\nTesting subprocess connect")
    test_subprocess()

    # Testing with a SyncManager object instead
    # Nonsensical with subprocesses
    print("\nTesting with a syncmanager namespace")
    test_multiprocess(mainc)
    """
    print("\nTesting with a syncmanager namespace")
    NS = Manager().Namespace()
    NS.A = A
    test_multiprocess(NS)
    print("Setting a new value")
    B = NS.A
    B.value = "a brand new value"
    NS.A = B
    test_multiprocess(NS)
    """

    SP.join()  # Hangs forever
