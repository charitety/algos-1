# Decompress

# Write a function, decompress, that takes in a string as an argument. 
# The input string will be formatted into multiple groups according to the following pattern:

# <number><char>
# for example, '2c' or '3a'.

# The function should return an decompressed version of the string where each 'char' of a group 
# is repeated 'number' times consecutively. 
# You may assume that the input string is well-formed according to the previously mentioned pattern.

def decompress(s):
    #create empty string to hold new string
    #loop through the input string
    #for each number, concatenate the subsequent letter the same number of time
    newString = ""
    factor = ""
    subString = ""

    for char in s:
        if char.isnumeric():
            factor += char
            # print(factor)
            # print(newString)
        else:
            char.isalpha()
            subString = (char)*int(factor)
            newString += subString
            factor = ""
            # print(subString)
    return newString


# TEST CASES
print(decompress("2c3a1t")) # -> 'ccaaat'
print(decompress("4s2b")) # -> 'ssssbb'
print(decompress("2p1o5p")) # -> 'ppoppppp'
print(decompress("3n12e2z")) # -> 'nnneeeeeeeeeeeezz'
print(decompress("127y")) # -> 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
