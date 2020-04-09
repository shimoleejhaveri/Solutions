"""
Given two strings S and T, return if they are equal when both are typed into 
empty text editors. # means a backspace character.

Example 1:
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:
Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:
Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:
Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

Note:
1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.

Follow up:
Can you solve it in O(N) time and O(1) space?
"""

def checkCharacter(string: str) -> str:
        
        char = "#"
        i = 0
        new_string=string
        
        while char in new_string: 
            if i == 0 and new_string[i] == char:
                new_string = new_string[1:]
            elif new_string[i] == char and i >= 1:
                new_string = new_string[0:i-1] + new_string[i+1:]
                i -= 1
            else:
                i += 1

        return new_string
        
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        new_S = checkCharacter(S)
        new_T = checkCharacter(T)

        if new_S == new_T:
            return True
        return False