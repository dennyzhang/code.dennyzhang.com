# Leetcode: Top K Frequent Words     :BLOG:Basic:


---

Top K Frequent Words  

---

Similar Problems:  
-   Tag: [#basic](https://brain.dennyzhang.com/category/basic)

---

Given a non-empty list of words, return the k most frequent elements.  

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.  
Example 1:  

    Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
    Output: ["i", "love"]
    Explanation: "i" and "love" are the two most frequent words.
        Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:  

    Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
    Output: ["the", "is", "sunny", "day"]
    Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
        with the number of occurrence being 4, 3, 2 and 1 respectively.

Note:  
1.  You may assume k is always valid, 1 <= k <= number of unique elements.
2.  Input words contain only lowercase letters.

Follow up:  
Try to solve it in O(n log k) time and O(n) extra space.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/top-k-frequent-words)  

Credits To: [leetcode.com](https://leetcode.com/problems/top-k-frequent-words/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/top-k-frequent-words
    ## Basic Ideas: Hash map
    ##            Count the occurency for different words
    ##            Then sort the list by descending occurency
    ## Complexity:
    import collections
    class Solution(object):
        def topKFrequent(self, words, k):
            """
            :type words: List[str]
            :type k: int
            :rtype: List[str]
            """
            m = collections.defaultdict(lambda: 0)
            for word in words:
                m[word] += 1
            key_list = m.keys()
            def myCompare(v1, v2):
                if m[v1] > m[v2]: return -1
                elif m[v1] < m[v2]: return 1
                else:
                    if v1 == v2: return 0
                    return -1 if v1 < v2 else 1
            sorted_list = sorted(key_list, cmp=myCompare)
            return sorted_list[0:k]
    
    s = Solution()
    print s.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4)