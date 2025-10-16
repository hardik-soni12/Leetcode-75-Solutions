'''You are given two strings word1 and word2. Merge the strings by adding letters in alternating 
order, starting with word1. If a string is longer than the other, append the additional letters 
onto the end of the merged string.Return the merged string.'''

'''
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
'''

def merge_alternatively(word1, word2):

    i = 0 

    len_w1 = len(word1)
    len_w2 = len(word2)
    merged = ''
    while i < len_w1 and i < len_w2:
        merged += word1[i] + word2[i]
        i += 1
    
    if i < len_w1:
        merged += word1[i:]

    if i < len_w2:
        merged += word2[i:]
    
    return merged

word1 = 'ab'
word2 = 'pqrs'
result = merge_alternatively(word1, word2)
print(result)