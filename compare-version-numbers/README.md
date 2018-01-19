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

Blog link: <http://brain.dennyzhang.com/compare-version-numbers>  

Github: challenges-leetcode-interesting  

Credits To: leetcode.com  

Leave me comments, if you know how to solve.  

    ## Basic Ideas: Pad two versions to the same count of segment
    ##     1.2.3 vs 1.3 -> 1.2.3 vs 1.3.0
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
            len1, len2 = len(l1), len(l2)
            max_len = max(len1, len2)
            for i in xrange(max_len):
                v1 = int(l1[i]) if i<len1 else 0
                v2 = int(l2[i]) if i<len2 else 0
                if v1 > v2: return 1
                elif v1 < v2: return -1
            return 0
    
    s = Solution()
    print s.compareVersion('01', '1') # 0
    print s.compareVersion('1.0', '1') # 0