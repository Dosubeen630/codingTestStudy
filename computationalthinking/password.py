letter = "HELLO Python"
encodeLetter =""

for ch in letter:
    num = ord(ch)
    encodeLetter += chr(num+1)

print("원문:", letter)
print("암호:", encodeLetter)


decodeLetter = ""

for ch in encodeLetter :
    num = ord(ch)
    decodeLetter += chr(num-1)

print("암호해제:", decodeLetter)    