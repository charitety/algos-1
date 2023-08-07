# Anagrams

# Write a function, anagrams, that takes in two strings as arguments. 
# The function should return a boolean indicating whether or not the strings are anagrams. 
# Anagrams are strings that contain the same characters, but in any order.

def anagrams(s1, s2):
  #add condition to discard false cases where lenght is different
  if len(s1) != len(s2):
    return False
  #create to lists of all the letters in each strings
  string1 = [char for char in s1]
  string2 = [char for char in s2]

  #order lists to get them ready to compare
  string1.sort()
  string2.sort()

  #compare the two lists
  if string1 == string2:
  #if the lists are equal, return True, 
    return True
  #if they are different, return False
  else:
    return False


# # TEST CASES
print(anagrams('restful', 'fluster'))# -> True
print(anagrams('cats', 'tocs'))# -> False
print(anagrams('monkeyswrite', 'newyorktimes')) # -> True
print(anagrams('paper', 'reapa')) # -> False
print(anagrams('elbow', 'below')) # -> True
print(anagrams('tax', 'taxi')) # -> False
print(anagrams('taxi', 'tax')) # -> False
print(anagrams('night', 'thing')) # -> True
print(anagrams('po', 'popp')) # -> False
print(anagrams('pp', 'oo')) # -> False
