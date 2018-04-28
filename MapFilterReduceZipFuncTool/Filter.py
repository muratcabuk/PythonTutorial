# Reemember: filter function must reruen always boolean

#Example 1

alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
def filterVowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if(alphabet in vowels):
        return True
    else:
        return False

filteredVowels=filter(filterVowels, alphabets)
print('The filtered vowels are:')
for vowel in filteredVowels:
    print(vowel)

#result: a e i


#Example with lambda (if you do not know lambda, please see Map.py file or readme.md)

numbers = [1,2,3,4,5,6,7,8,9]
checkedNumbers = filter(lambda x: x%2 == 0, numbers)
print(list(checkedNumbers))
#result: 2,4,6,8


#Example
myNumbers = ((1,2),(4,3),(5,6),(9,8))

biggerNumbers = filter(lambda c: True if (c[0] > c[1]) else False, map(lambda c:(c[0],c[1]),myNumbers))

print(list(biggerNumbers))

#result: [(4, 3), (9, 8)]


