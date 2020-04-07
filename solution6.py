"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:
All inputs will be in lowercase.
The order of your output does not matter.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        final_list = []
       
        if len(strs) == 0: 
            return final_list
        
        dic = {}
        
        for word in strs:
            chars = str(sorted(word))
            if chars in dic:
                dic[chars].append(word)
            else:
                dic[chars] = [word]
                
        for keys in dic:
            final_list.append(dic[keys])
            
        return final_list