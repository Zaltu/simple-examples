"""
Connect to a remote process and fetch a shared complex object.
"""
from multiprocessing.managers import BaseManager

def test_connect_remote():
    """
    Connect to remote process and load complex object.
    """
    BaseManager.register('get_my_class')
    rpm = BaseManager(address=('', 50000), authkey=b'abracadabra')
    rpm.connect()
    rpclass = rpm.get_my_class()
    rpclass.niceprint()

if __name__ == "__main__":
    test_connect_remote()
