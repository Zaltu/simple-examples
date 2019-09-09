"""
Tests for sharing complex objects between python processes.

Note that the mutliprocessing.managers create proxies, not really "endpoints",
so variable changes will not propagate
"""
from multiprocessing import Process
from multiprocessing.managers import BaseManager
import subprocess

from pprint import pprint as pp


class MyClass():
    """
    Dummy class with a test function using an external import
    """
    value = "print"
    def niceprint(self):
        """
        Dummy function
        """
        pp({"pretty": self.value})

A = MyClass()


def themanager():
    """
    Manager container. Pops open the inter-process server and serves it until killed.
    """
    BaseManager.register('get_my_class', callable=lambda: A)
    mana = BaseManager(address=('', 50000), authkey=b'abracadabra')
    server = mana.get_server()
    server.serve_forever()


def multicalled():
    """
    Meant to be called in a multiprocessing.Process for testing purposes.
    Connects to the managed queue from the original process and calls the stored value.
    """
    BaseManager.register('get_my_class')
    rpm = BaseManager(address=('', 50000), authkey=b'abracadabra')
    rpm.connect()
    rpclass = rpm.get_my_class()
    rpclass.niceprint()


def test_multiprocess():
    """
    Simplification of the steps to test mutliprocessing module connectivity
    """
    rp = Process(target=multicalled)
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
    SP = Process(target=themanager)
    SP.start()

    print("Testing multiprocess connect")
    test_multiprocess()

    print("Testing subprocess connect")
    test_subprocess()

    SP.join()  # Hangs forever
