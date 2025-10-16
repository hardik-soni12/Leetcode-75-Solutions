'''
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t 
(i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
'''

'''
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
'''

def gcd_of_strings(str1, str2):

    if str1 + str2 != str2 + str1:
        return ""
    
    def gcd(a, b):
        a, b = b, a % b
        return a
    
    size = gcd(len(str1), len(str2))
    return str1[:size]
    

example1 = gcd_of_strings('ABC', 'ABCABC')
example2 = gcd_of_strings('TEST', 'STRING')
print(example1)
print(example2)