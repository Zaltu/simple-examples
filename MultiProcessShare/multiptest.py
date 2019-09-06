from multiprocessing import Process, Queue
from multiprocessing.managers import BaseManager

from pprint import pprint as pp

class MyClass():
    def niceprint(self):
        pp({"pretty": "dict"})

a = MyClass()


class QueueManager(BaseManager):
    pass


def themanager():
    QueueManager.register('get_queue', callable=lambda: a)
    m = QueueManager(address=('', 50000), authkey=b'abracadabra')
    s = m.get_server()
    s.serve_forever()

def multicalled():
    QueueManager.register('get_queue')
    rpm = QueueManager(address=('', 50000), authkey=b'abracadabra')
    rpm.connect()
    rpqueue = rpm.get_queue()
    rpqueue.niceprint()

print("Launching Server process")

sp = Process(target=themanager)
sp.start()

print("Launching read process")

rp = Process(target=multicalled)
rp.start()

rp.join()
sp.join()
