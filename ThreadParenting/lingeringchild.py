import time
from threading import Thread



def haveBaby():
    t2 = Thread(target=waste)
    print("Starting 2")
    t2.start()


def waste():
    print("I gotta tell you something really important, it's...")
    time.sleep(1)
    print("the KFP recipe is <redacted>")


t1 = Thread(target=haveBaby, daemon=True)

print("Starting 1")
t1.start()
print("Attempting to join 1")
t1.join()
print("Joined 1")
