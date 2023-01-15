def validate(RomanNumber):
    vcount = lcount = dcount = 0
    for i in RomanNumber:
        if i * 4 in RomanNumber:
            return False
        elif i == "V":
            vcount += 1
        elif i == "L":
            lcount += 1
        elif i == "D":
            dcount += 1
        elif i not in "IVXLCDM":
            return False
        else:
            pass
    if vcount >= 2 or lcount >= 2 or dcount >= 2:
        return False
    else:
        return True


def RomanToDecimal(RomanNumber):
    romanNumFormat = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for digit in RomanNumber:
        for letter in romanNumFormat:
            if digit == letter:
                decimalList.append(romanNumFormat[letter])


def FormatAndPrint():
    i = 1
    sum = 0
    for digit in decimalList:
        if i >= len(decimalList):
            i = i - 1
        if digit < decimalList[i]:
            sum -= digit
        else:
            sum += digit
        i += 1
    print("Decimal Number:", sum)


def EnterRomanNumber():
    while True:
        RomanNumber = input("Roman Number:").upper()
        if validate(RomanNumber) == True:
            return RomanNumber
        else:
            print("\nInvalid!\nPlease Enter Again...\n")


decimalList = []
Rnumber=EnterRomanNumber()
RomanToDecimal(Rnumber)
FormatAndPrint()
