# Leetcode: Minimum Genetic Mutation     :BLOG:Medium:


---

Minimum Genetic Mutation  

---

Similar Problems:  
-   [Word Ladder](https://brain.dennyzhang.com/word-ladder)
-   [Open the Lock](https://brain.dennyzhang.com/open-the-lock)
-   [Review: BFS Problems](https://brain.dennyzhang.com/review-bfs)

---

A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".  

Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.  

For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.  

Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.  

Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.  

Note:  

1.  Starting point is assumed to be valid, so it might not be included in the bank.
2.  If multiple mutations are needed, all mutations during in the sequence must be valid.
3.  You may assume start and end string is not the same.

Example 1:  

    start: "AACCGGTT"
    end:   "AACCGGTA"
    bank: ["AACCGGTA"]
    
    return: 1

Example 2:  

    start: "AACCGGTT"
    end:   "AAACGGTA"
    bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    
    return: 2

Example 3:  

    start: "AAAAACCC"
    end:   "AACCCCCC"
    bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
    
    return: 3

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/minimum-genetic-mutation)  

Credits To: [leetcode.com](https://leetcode.com/problems/minimum-genetic-mutation/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/minimum-genetic-mutation
    ## Basic Ideas: BFS + Set
    ##
    ## Complexity: Time O(1), Space O(1)
    ##     We will only have 8 characters. pow(4, 8) is still O(1)
    ##
    class Solution(object):
        def minMutation(self, start, end, bank):
            """
            :type start: str
            :type end: str
            :type bank: List[str]
            :rtype: int
            """
            import collections
            valid_set = set(bank)
    
            if start == end:
                return 0 if start in valid_set else -1
            if end not in valid_set: return -1
    
            seen = set([])
            queue = collections.deque()
            queue.append(start)
            seen.add(start)
            level = 0
            while len(queue) != 0:
                level += 1
                for k in range(len(queue)):
                    node = queue.popleft()
                    # find neighbors
                    for i in range(8):
                        for ch in "ACGT":
                            if ch == node[i]: continue
                            node2 = "%s%s%s" % (node[:i], ch, node[i+1:])
                            if node2 not in seen and node2 in valid_set:
                                if node2 == end: return level
                                queue.append(node2)
                                seen.add(node2)
            return -1