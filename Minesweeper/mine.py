from pprint import pprint as pp
from random import randint



def genField(x, y):
    field = []
    for i in range(0, x):
        field.append([])
        for j in range(0, y):
            field[i].append(0)
    return field

def placeBs(field, n):
    xd = len(field)
    yd = len(field[0])
    generatedPos = []

    while len(generatedPos) < n:
        xr = randint(0, xd-1)
        yr = randint(0, yd-1)
        if (xr, yr) not in generatedPos:
            field[xr][yr] = "B"
            generatedPos.append((xr, yr))

    return field


def setCount(field):
    for i in range(0, len(field)):
        for j in range(0, len(field[i])):
            closeCounter = 0
            print("Counting %s %s" % (i, j))
            for irange in range(i-1, i+2):
                for jrange in range(j-1, j+2):
                    if irange < 0 or jrange < 0:
                        continue
                    try:
                        print("Checking %s %s" % (irange, jrange))
                        if field[irange][jrange] == "B":
                            print("Found Bomb")
                            closeCounter += 1
                    except IndexError:
                        continue
            print()
            if field[i][j] != "B":
                field[i][j] = closeCounter


if __name__ == "__main__":
    f = genField(5, 5)
    placeBs(f, 3)
    setCount(f)
    pp(f)
