"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
"""

def longestPalindrome(s):
    m = ''
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            if len(m) >= j-i:
                break
            elif s[i:j] == s[i:j][::-1]:
                m = s[i:j]
                break
    return m

input = "babad"
print(longestPalindrome(input))

"""
Variable        |       Value
s               |       "babad"
m               |       "bab"
i               |       4
j               |       5
                |
return value    |       "bab"
"""