'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
 of the characters without disturbing the relative positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
'''

'''
example:
Input: s = "abc", t = "ahbgdc"
Output: true
'''

def isSubsequence(s,t):
    count = 0
    for i in t:
        if count < len(s) and s[count] == i:
            count += 1

    return count == len(s)

s = "abc"
t = "ahbgdc"
print(isSubsequence(s,t))