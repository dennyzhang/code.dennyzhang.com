# Leetcode: Generalized Abbreviation     :BLOG:Medium:


---

Generalized Abbreviation  

---

Similar Problems:  
-   [Letter Case Permutation](https://brain.dennyzhang.com/letter-case-permutation)
-   [Review: Combinations and Permutations Problems](https://brain.dennyzhang.com/review-combination)

---

Write a function to generate the generalized abbreviations of a word.  

Example:  
Given word = "word", return the following list (order does not matter):  
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/generalized-abbreviation)  

Credits To: [leetcode.com](https://leetcode.com/problems/generalized-abbreviation/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/generalized-abbreviation
    ## Basic Ideas: BFS
    ##
    ## Complexity: Time O(n*pow(2,n)), Space O(pow(2, n))
    class Solution:
        def generateAbbreviations(self, word):
            """
            :type word: str
            :rtype: List[str]
            """
            import collections
            queue = collections.deque()
            queue.append([""])
            for ch in word:
                for k in range(len(queue)):
                    element = queue.popleft()
                    if element[-1] == "":
                        queue.append([ch])
                        queue.append(["1"])
                    elif element[-1].isdigit():
                        queue.append(element + [ch])
                        queue.append(element[:-1] + [str(int(element[-1])+1)])
                    else:
                        queue.append(element + [ch])
                        queue.append(element + ["1"])
            res = []
            for element in queue: res.append(''.join(element))
            return res