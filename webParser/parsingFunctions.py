import os

def parseFile(filePath):
    # create additional functions as needed
    # comment a shit ton
    return
    

# for testing only
# to login into my eclass do "python .\main.py"
# to run this file do "python .\parsingFunctions.py"
fileDir = os.path.dirname(os.path.realpath('__file__'))
filePath = os.path.join(fileDir, f"parseMaterials/test.txt")
parseFile(filePath)