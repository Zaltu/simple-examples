"""
Various actions that can be performed
"""
import re
import subprocess

COMS = [".com", ".net", ".org", ".io", ".gg"]
OMIT_WORDS = {"of", "a", "the", "for"}


def basicArithmatic(strEquation):
    """
    Perform basic arithmatic. Eval is used since it's far easier than parsing string equations. Doesn't make
    it any safer though.

    :param str strEquation: string mathematic expression to evaluate

    :returns: evaluated expression
    :rtype: int|float
    """
    return eval(strEquation)  #pylint: disable=eval-used


def searchSpecific(keywords):
    """
    Launch a browser prepped with a search for something or other.

    :param str keywords: search terms

    :returns: confirmation of successful launch w/ the subprocess PID
    :rtype: str
    """
    search = subprocess.Popen(['firefox', 'https://www.google.com/search?q=%s'%keywords])
    return "Search launched! Process %s" % search.pid


def execute(program, keywords=None):
    """
    Launch an arbitrary program. Assumes the program is in the path. No validation is done.

    :param str program: execution command of program to launch
    :param str keywords: any arguments to be passed to the program on launch, defaults to None

    :returns: confirmation of successful launch w/ subprocess PID
    :rtype: str
    """
    program = subprocess.Popen([program, keywords] if keywords else [program])
    return "%s launched! Process %s" % (program, program.pid)


def searchImageSpecific(keywords):
    """
    Launch a browser with a Google image search.

    :param str keywords: keywords for search

    :returns: confirmation of successful launch w/ subprocess PID
    :rtype: str
    """
    search = subprocess.Popen(['firefox', 'https://www.google.com/search?q=%s&tbm=isch'%keywords])
    return "Search launched! Process %s" % search.pid


def openSite(site):
    """
    Launch a browser on a given web page.

    :param str site: webstie to open

    :returns: confirmation of successful launch w/ subprocess PID
    :rtype: str
    """
    browser = subprocess.Popen(['firefox', 'https://%s'%site])
    return "Site opened! Process %s" % browser.pid


def youtubeSearch(keywords):
    """
    Launch a browser with the results of a youtube search.

    :param str keywords: keywords for search

    :returns: confirmation of successful launch w/ subprocess PID
    :rtype: str
    """
    search = subprocess.Popen(['firefox', 'https://www.youtube.com/search?q=%s'%keywords])
    return "Search launched! Process %s" % search.pid


def opener(keywords, terms=""):
    """
    Really bad function wrapping the "execute" action to generate the argument parameters used to launch the
    program. No idea why I did this at the time, and obviously I didn't comment it. I mean, who do you think
    I am?

    :param str keywords: keywords used to identify the action to take
    :param str terms: stuff actually used to launch the program and it's arguments

    :returns: the result of execute, or a message that the requested program is invalid
    :rtype: str
    """
    for com in COMS:
        if com in keywords:
            ewOp = keywords.split(" ")
            for chunk in ewOp:
                if com in chunk:
                    site = chunk
            return openSite(site)
    command = terms.split(" ")
    print(command)
    try:
        return execute(command[0], command[1:] or None)
    except OSError:
        return "That program isn't in the PATH..."


def interface(commandKeyword, command, fullTerms):
    """
    Interface between the actions and the call from the upper scope for some reason. I think to manage the
    varying parameters. This code is terrible.

    :param str commandKeyword: the keyword used to determine which action to take
    :param str command: the command function
    :param str fullTerms: the full input

    :returns: the result of calling the command
    :rtype: object
    """
    fullTerms = re.sub('[!@#$,:;?]', '', fullTerms)
    words = set(fullTerms.split(" "))
    terms = words.difference(set(commandKeyword.split(" "))).difference(OMIT_WORDS)
    print("Command: %s\nFunction: %s\nKeywords: %s" % (commandKeyword, command, terms))
    if command is opener:
        # This is the cancer :stringmanipulation:
        return command(
            ' '.join(terms),
            ' '.join(fullTerms.split(" ")[fullTerms.split(" ").index(commandKeyword)+1:])
        )
    return command(' '.join(terms))



if __name__ == "__main__":
    print(basicArithmatic("3*4+1"))
    print(searchImageSpecific("test"))
