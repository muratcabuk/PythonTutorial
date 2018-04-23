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
biggerNumbers = filter(lambda x: x[0] if (x[0] > x[1]) else x[1], map(lambda c:(c[0],c[1]),myNumbers))

