
def chunksToMaxChars(s):
    if len(s) < 10:
        yield s
        return
    splitstr = s.split(" ")
    print(splitstr)
    i = 0
    while i < len(splitstr):
        beginOffset = i
        while len(" ".join(splitstr[beginOffset:i])) < 10 and i < len(splitstr):
            i += 1
        yield " ".join(splitstr[beginOffset:i])



for chunk in chunksToMaxChars("Hello there my good friend. How are you on this fine day?"):
    print("CHUNKED: %s" % chunk)
