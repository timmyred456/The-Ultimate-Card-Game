from CardCode.TextManagment.SlowType import *
from CardCode.TextManagment.jsonRead import *
from CardCode.TextManagment.objectGUIs import *

def CheckBetween(String,Seperators):
    ExtractedString = ""
    ExtractedData = []
    StringSplit = list(String)
    Nested = False
    curExLine = 0

    for char in range(len(StringSplit)):
        if StringSplit[char] == Seperators[0]: # If char is the start of data extraction
            Nested = True
            curExLine = char
        elif StringSplit[char] == Seperators[1]: # If char is end of data extraction, finish with current data
            Nested = False
            ExtractedData.append([ExtractedString,curExLine])
            ExtractedString = ""
        elif Nested == True: # While Extracting chars
            ExtractedString += StringSplit[char]

    return ExtractedData