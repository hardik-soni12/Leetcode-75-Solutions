'''
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
'''

'''
Input: s = "IceCreAm"
Output: "AceCreIm"

Explanation:
The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".
'''

def reverse_vowels(s):
    vowels = 'aeiouAEIOU'
    vowel_list = [c for c in s if c in vowels][::-1]
    res = []
    for char in s:
        if char in vowels:
            res.append(vowel_list.pop(0))
        else:
            res.append(char)
    return ''.join(res)

s = "IceCreAm"
print(reverse_vowels(s))