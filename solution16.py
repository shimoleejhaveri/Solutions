"""
Given a string containing only three types of characters: '(', ')' and '*', 
write a function to check whether this string is valid. We define the validity 
of a string by these rules:

1. Any left parenthesis '(' must have a corresponding right parenthesis ')'.
2. Any right parenthesis ')' must have a corresponding left parenthesis '('.
3. Left parenthesis '(' must go before the corresponding right parenthesis ')'.
4. '*' could be treated as a single right parenthesis ')' or a single left parenthesis 
    '(' or an empty string.
5. An empty string is also valid.

Example 1:
Input: "()"
Output: True

Example 2:
Input: "(*)"
Output: True

Example 3:
Input: "(*))"
Output: True

Note:
The string size will be in the range [1, 100].
"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        if not s:
            return True
        
        s1 = []
        s2 = []
        
        for i in range(len(s)):
            if s[i] == "(":
                s1.append(i)
            elif s[i] == "*":
                s2.append(i)
            elif s[i] == ")":
                if s1:
                    s1.pop(-1)
                else:
                    if s2:
                        s2.pop(-1)
                    else:
                        return False
        
        while s1:
            if not s2:
                return False
            else:
                if s1.pop(-1) > s2.pop(-1):
                    return False
        return True