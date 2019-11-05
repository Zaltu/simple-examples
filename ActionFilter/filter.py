"""
Top-level launcher for action filter example.
"""
from smarts import actions

COMMAND_KEYWORDS = {
    "calculate":actions.basicArithmatic,
    "search":actions.searchSpecific,
    "search video":actions.youtubeSearch,
    "search videos":actions.youtubeSearch,
    "search image":actions.searchImageSpecific,
    "search images":actions.searchImageSpecific,
    "search picture":actions.searchImageSpecific,
    "search pictures":actions.searchImageSpecific,
    "search pic":actions.searchImageSpecific,
    "search pics":actions.searchImageSpecific,
    "open":actions.opener,
    "open up":actions.opener,
    "launch":actions.opener
}


def textFilter(text):
    """
    Find the keyword from the list of keywords that is the best match to the input. Best match means *most
    space-delimited elements found in common between the input and the key*. Works surprisingly well.
    Basically an extremely dumbed down "natural language processor", heavily air-quoted.

    :param str text: input text
    """
    words = set(text.split(" "))
    most = 0
    command = None
    for key in COMMAND_KEYWORDS:
        #print(set(key.split(" ")))
        #print(words)
        #print(set(key.split(" ")).intersection(words))
        #print(most)
        intNum = len(set(key.split(" ")).intersection(words))
        #print(intNum)
        if most < intNum or\
        (most == intNum and len(set(key.split(" ")))<len(set(command.split(" "))) if command else 0):
            most = intNum
            command = key

    comRet = None
    if command:
        comRet = actions.interface(command, COMMAND_KEYWORDS[command], text)

    prin = "Answer :)\n"
    if comRet:
        prin += str(comRet)
    print(prin)



if __name__ == "__main__":
    import sys
    textFilter(sys.argv[1])
    #textFilter("calculate 4*13/2+1")
    #textFilter("hey, open www.github.com please")
    #textFilter("image search very fast of dog running at incredibly high speed")
