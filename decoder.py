
f = open("text.data", 'r+')
line = f.read()
#line = "d3e61424adb3f5"
hexChar = ""

binList= []
for hexi in range(len(line)):
    hexChar += str(line[hexi])
    if hexi %2 == 1:
        binList.append(bin(int(hexChar, 16))[2:].zfill(8))
        hexChar = ""
decodedList = []
tempInt = 0
#binList=['bAAAAAAA', 'ccBBBBBB', 'dddCCCCC', 'eeeeDDDD', 'fffffEEE', 'ggggggFF', 'hhhhhhhG']

for binIndentifier in range(len(binList)):
    tempInt = 0
    identifier = binIndentifier% 7
    if identifier == 6:
        tempInt = "0" + binList[binIndentifier][identifier + 1:8] + binList[binIndentifier - 1][0:identifier]
        tempInt = int(tempInt, 2)
        decodedList.append(tempInt)
        tempInt = "0"+binList[binIndentifier][0:7]
        tempInt= int(tempInt,2)
    else:
        tempInt = "0" + binList[binIndentifier][identifier+1:8] + binList[binIndentifier - 1][0:identifier]
        tempInt = int(tempInt, 2)
    decodedList.append(tempInt)
for char in range(len(decodedList)):
    decodedList[char] = chr(int(decodedList[char]))
message = ""
for char in decodedList:
    message += char
print message
   # charList.a
# old code
# for binIdentifier in range(len(binary)):
#     identifier = binIdentifier%8
#     if identifier == 0:
#         pass
#     elif identifier == 0:
#         pass
#     else:
#         newValue = str(binary[binIdentifier][8-(identifier):8]) + str(binary[binIdentifier-1][1:(9  -identifier)])
#         print binary[binIdentifier][8-(identifier+1):8]
#         print
#         bit7List.append(newValue)
# print bit7List
# hexList = []
# for bins in bit7List:
#     hexList.append(hex(int(bins, 2)))
# print hexList