# Leetcode: Compare Version Numbers     :BLOG:Amusing:


---

Compare Version Numbers  

---

Compare two version numbers version1 and version2.  
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.  

You may assume that the version strings are non-empty and contain only digits and the . character.  
The . character does not represent a decimal point and is used to separate number sequences.  
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.  

Here is an example of version numbers ordering:  

0.1 < 1.1 < 1.2 < 13.37  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/compare-version-numbers)  

Credits To: [Leetcode.com](https://leetcode.com/problems/compare-version-numbers/description/)  

Leave me comments, if you know how to solve.  

    class Solution(object):
    ## Basic Ideas:
    ##     1.1 < 1.1.2
    ##     1.1 == 1.1.0
    ## Complexity:
    class Solution(object):
        def compareVersion(self, version1, version2):
            """
            :type version1: str
            :type version2: str
            :rtype: int
            """
            l1, l2 = version1.split('.'), version2.split('.')
            i = 0
            while i < len(l1) and i < len(l2):
                if int(l1[i]) > int(l2[i]):
                    return 1
                elif int(l1[i]) < int(l2[i]):
                    return -1
                i += 1
    
            if i == len(l1) and i == len(l2):
                return 0
            else:
                res = 1
                if i == len(l2):
                    l = l1[i:]
                else:
                    l = l2[i:]
                    res = -1
    
                for element in l:
                    if int(element) != 0:
                        return res
                return 0
    
    s = Solution()
    print s.compareVersion('01', '1') # 0
    print s.compareVersion('1.0', '1') # 0