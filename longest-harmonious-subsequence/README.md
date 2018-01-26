# Leetcode: Longest Harmonious Subsequence     :BLOG:Basic:


---

Longest Harmonious Subsequence  

---

We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.  

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.  

    Example 1:
    Input: [1,3,2,2,5,2,3,7]
    Output: 5
    Explanation: The longest harmonious subsequence is [3,2,2,2,3].

Note: The length of the input array will not exceed 20,000.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/longest-harmonious-subsequence)  

Credits To: [leetcode.com](https://leetcode.com/problems/longest-harmonious-subsequence/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/longest-harmonious-subsequence
    ## Basic Ideas: The input array won't exceed 20,000
    ##              Build a map from the array. key is the number in the list, value is the occurence count
    ##              For each key in the map, check m.get(key+1)
    ##              Here we don't need to compare m.get(key-1). 
    ##              Why? We will also visit the smaller value sooner or later
    ##
    ## Complexity: Time O(n), Space O(n)
    ##
    ##             If the array is too long, sort it. And use two pointers to get the number. 
    ##             Then the complexity would be Time O(n*long(n)), Space O(1)
    import collections
    class Solution(object):
        def findLHS(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            m = collections.defaultdict(lambda: 0)
            for num in nums:
                m[num]+=1
    
            max_count = 0
            for num in nums:
                if num+1 in m:
                    max_count = max(max_count, m[num]+m[num+1])
            return max_count