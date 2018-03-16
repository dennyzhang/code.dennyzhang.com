# Leetcode: Group Anagrams     :BLOG:Medium:


---

Given an array of strings, group anagrams together.  

---

Similar Problems:  
-   [Group Shifted Strings](https://brain.dennyzhang.com/group-shifted-strings)
-   [Tag: #hashmap](https://brain.dennyzhang.com/tag/hashmap)

---

Given an array of strings, group anagrams together.  

    For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
    Return:
    
    [
      ["ate", "eat","tea"],
      ["nat","tan"],
      ["bat"]
    ]

Note: All inputs will be in lower-case.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/group-anagrams)  

Credits To: [leetcode.com](https://leetcode.com/problems/group-anagrams/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/group-anagrams
    ## Basic Ideas:  map each item to a string, group them by a map, dump the map
    ## Complexity: Time O(n*k*log(k)), Space O(k*n). k is the length of longest item
    class Solution(object):
        def groupAnagrams(self, strs):
            """
            :type strs: List[str]
            :rtype: List[List[str]]
            """
            m = {}
            for item in strs:
                sorted_item = ''.join(sorted(item))
                if m.has_key(sorted_item):
                    m[sorted_item].append(item)
                else:
                    m[sorted_item] = [item]
    
            res = []
            for key in m:
                res.append(m[key])
            return res