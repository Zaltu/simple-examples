"""
Example to chunk a sentence into 10 characters, rounding up to the nearest word.
"""
#pylint: disable=missing-yield-doc,missing-yield-type-doc,invalid-name
def chunksToMaxChars(s, chunksize):
    """
    Chunk string to number of characters, rounding up to nearest space.

    :param string s: string to chunk
    :param int chunksize: number of chars to chunk to

    :yields str: chunk of given string
    """
    if len(s) < chunksize:
        yield s
        return
    splitstr = s.split(" ")
    print(splitstr)
    i = 0
    while i < len(splitstr):
        beginOffset = i
        while len(" ".join(splitstr[beginOffset:i])) < chunksize and i < len(splitstr):
            i += 1
        yield " ".join(splitstr[beginOffset:i])


# Test iterator
CHUNKSIZE = 10
for chunk in chunksToMaxChars("Hello there my good friend. How are you on this fine day?", CHUNKSIZE):
    print("CHUNKED: %s" % chunk)
