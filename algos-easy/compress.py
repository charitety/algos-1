# Compress

# Write a function, compress, that takes in a string as an argument. 
# The function should return a compressed version of the string where consecutive occurrences of 
# the same characters are compressed into the number of occurrences followed by the character. 
# Single character occurrences should not be changed.

# 'aaa' compresses to '3a'
# 'cc' compresses to '2c'
# 't' should remain as 't'

# You can assume that the input only contains alphabetic characters.


def compress(s):
    pass # TODO:

#Iterate through the string starting at first letter, index 0
#Declare a counter at 0 and a new string
#If the following letter is NOT equal than the previous, append the letter only to the new string
#If the letter is equal to previous, increment counter and keep iterating
#When a new letter if found, append string counter and previous letter to new string
#Reset counter and keepp iteraring


# TEST CASES
compress('ccaaatsss') # -> '2c3at3s'
# compress('ssssbbz') # -> '4s2bz'
# compress('ppoppppp') # -> '2po5p'
# compress('nnneeeeeeeeeeeezz') # -> '3n12e2z'
# compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy');  # -> '127y'
