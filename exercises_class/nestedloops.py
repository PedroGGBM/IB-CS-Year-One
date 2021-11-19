
def lowercase(aString):
    if chr(aString) in range(65, 91):
        return ord(chr(aString)+32)
    else:
        return aString

print(lowercase("A"))