"""

Usage:
  7bit e (-s=STRING | -f=FILE)
  7bit d <string>
  7bit --version
  7bit--help

Options:
  --help                        Show this screen.
  --version                     Show the version.
  -s STRING, --string STRING             Encode the string
  -f FILE, --file FILE               Encode the file
"""
from docopt import docopt
VERSION="ALPHA"

def encode(line):
    binary = []
    bit7List = []
    spacesNeeded=len(line)%8
    if spacesNeeded != 0:
        for i in range (8-spacesNeeded):
            line += " "
    for i in range(len(line)):
        binary.append(format(ord(line[i]), 'b').zfill(8))
    for binIdentifier in range(len(binary)):
        identifier = binIdentifier % 8
        if identifier == 0:
            pass
        elif identifier == 0:
            pass
        else:
            newValue = str(binary[binIdentifier][8 - (identifier):8]) + str(
                binary[binIdentifier - 1][1:(9 - identifier)])
            bit7List.append(newValue)
    hexList = []
    for bins in bit7List:
        hexList.append(hex(int(bins, 2)))
    message = printList(hexList)
    print message

def decode(line):
    hexChar = ""
    binList = []
    for hexi in range(len(line)):
        hexChar += str(line[hexi])
        if hexi % 2 == 1:
            binList.append(bin(int(hexChar, 16))[2:].zfill(8))
            hexChar = ""
    decodedList = []
    tempInt = 0

    for binIndentifier in range(len(binList)):
        tempInt = 0
        identifier = binIndentifier % 7
        if identifier == 6:
            tempInt = "0" + binList[binIndentifier][identifier + 1:8] + binList[binIndentifier - 1][0:identifier]
            tempInt = int(tempInt, 2)
            decodedList.append(tempInt)
            tempInt = "0" + binList[binIndentifier][0:7]
            tempInt = int(tempInt, 2)
        else:
            tempInt = "0" + binList[binIndentifier][identifier + 1:8] + binList[binIndentifier - 1][0:identifier]
            tempInt = int(tempInt, 2)
        decodedList.append(tempInt)
    for char in range(len(decodedList)):
        decodedList[char] = chr(int(decodedList[char]))
    message = printList(decodedList)
    print message

def printList(list):
    message = ""
    for char in list:
        message += char
    return message


arguments = docopt(__doc__, version=VERSION)
print arguments
if arguments["e"]:
    #do the encode
    if encode(arguments["--file"]):
        file_string= open(arguments["--file"]).read()
        encode(file_string)
    else:
        encode(arguments["<string>"])
elif arguments["d"]:
    #do the decode
    decode(arguments["<string>"])
else:
    print arguments