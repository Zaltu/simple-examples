"""
Quick and simple way of updating the formatting of ugly JSON files.
"""
import os
import glob
import json

def getFiles(folderpath):
    """
    Get the JSON files from a certain path.

    :param str folderpath: folder to fetch

    :returns: files in that folder
    :rtype: list
    """
    return glob.glob(os.path.join(folderpath, "*.json"))


def convertFile(filepath):
    """
    Load a file as JSON and rewrite it with an indent.

    :param str filepath: path of file to beautify
    """
    with open(filepath, "r+") as toconvert:
        loaded = json.loads(toconvert.read())
        toconvert.seek(0)
        toconvert.write(json.dumps(loaded, indent=4))


def main(folderpath):
    """
    Read the JSON files in a given folder and rewrite them with good formatting.

    :param str folderpath: folder containing JSON files
    """
    files = getFiles(folderpath)
    for f in files:
        print(f)
        convertFile(f)

# Set folder path here.
main("")
