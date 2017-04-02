f = open("text.data", 'r+')
line = f.read()
line = "SMS Rulz"
binary = []
bit7List =[]
for i in range(len(line)):
    binary.append(format(ord(line[i]), 'b').zfill(8))
#binary = ["XAAAAAAA","XBBBBBBb","XCCCCCcc","XDDDDddd","XEEEeeee","XFFfffff","XGgggggg","Xhhhhhhh"]
print binary
for binIdentifier in range(len(binary)):
    identifier = binIdentifier%8
    if identifier == 0:
        pass
    elif identifier == 0:
        pass
    else:
        newValue = str(binary[binIdentifier][8-(identifier):8]) + str(binary[binIdentifier-1][1:(9  -identifier)])
        print binary[binIdentifier][8-(identifier+1):8]
        print
        bit7List.append(newValue)
print bit7List
hexList = []
for bins in bit7List:
    hexList.append(hex(int(bins, 2))[2:])
print hexList
