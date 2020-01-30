"""
Simple example of generating a minesweeper field.
"""
#pylint: disable=invalid-name
from pprint import pprint as pp
from random import randint


def genField(x, y):
    """
    Generate a field of a certain dimension.

    :param int x: x dimension
    :param int y: y dimension

    :returns: empty field
    :rtype: list
    """
    field = []
    for i in range(0, x):
        field.append([])
        for j in range(0, y):
            field[i].append(0)
    return field


def placeBs(field, n):
    """
    Place n bombs in random spots on the field.

    :param list field: the field
    :param int n: number of bombs to place
    """
    xd = len(field)
    yd = len(field[0])
    generatedPos = []

    while len(generatedPos) < n:
        xr = randint(0, xd-1)
        yr = randint(0, yd-1)
        if (xr, yr) not in generatedPos:
            field[xr][yr] = "B"
            generatedPos.append((xr, yr))


def setCount(field):
    """
    Generate the bomb count for every non-bomb square on the field.

    :param list field: the field
    """
    for i in range(0, len(field)):
        for j in range(0, len(field[i])):
            closeCounter = 0
            #print("Counting %s %s" % (i, j))
            for irange in range(i-1, i+2):
                for jrange in range(j-1, j+2):
                    # This is because python list indexes wrap on negative values.
                    # Can be an interesting mechanic though lol
                    if irange < 0 or jrange < 0:
                        continue
                    try:
                        #print("Checking %s %s" % (irange, jrange))
                        if field[irange][jrange] == "B":
                            #print("Found Bomb")
                            closeCounter += 1
                    except IndexError:
                        continue
            #print()
            if field[i][j] != "B":
                field[i][j] = closeCounter


if __name__ == "__main__":
    f = genField(5, 5)
    placeBs(f, 3)
    setCount(f)
    pp(f)
