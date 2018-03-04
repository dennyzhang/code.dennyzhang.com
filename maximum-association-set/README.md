# LintCode: Maximum Association Set     :BLOG:Medium:


---

Maximum Association Set  

---

Similar Problems:  
-   [Review: BFS Problems](https://brain.dennyzhang.com/review-bfs), [Tag: #bfs](https://brain.dennyzhang.com/tag/bfs)

---

Amazon sells books, every book has books which are strongly associated with it. Given ListA and ListB,indicates that ListA [i] is associated with ListB [i] which represents the book and associated books. Output the largest set associated with each other(output in any sort). You can assume that there is only one of the largest set.  

Notice  
-   The number of books does not exceed 5000.

Example  

    Given ListA = ["abc","abc","abc"], ListB = ["bcd","acd","def"], return["abc","acd","bcd","dfe"].
    
    Explanation:
    abc is associated with bcd, acd, dfe, so the largest set is the set of all books

    Given ListA = ["a","b","d","e","f"], ListB = ["b","c","e","g","g"], return ["d","e","f","g"].
    
    Explanation:
    The current set are [a, b, c] and [d, e, g, f], then the largest set is [d, e, g, f]

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/maximum-association-set)  

Credits To: [LintCode.com](http://www.lintcode.com/en/problem/maximum-association-set/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/maximum-association-set
    #!/usr/bin/env python
    class Solution:
        """
        @param ListA: The relation between ListB's books
        @param ListB: The relation between ListA's books
        @return: The answer
        """
        def maximumAssociationSet(self, ListA, ListB):
            # Write your code here
            ## Basic Ideas: Use hashmap
            ## Complexity: Time O(n), Space O(n)
            m = {}
            length = len(ListA)
            # Build relationship
            for i in range(0, length):
                bookA, bookB = ListA[i], ListB[i]
                if bookA in m:
                    m[bookA].add(bookB)
                else:
                    m[bookA] = set([bookB])
    
                if bookB in m:
                    m[bookB].add(bookA)
                else:
                    m[bookB] = set([bookA])
    
            visited = set([])
            max_count, res = 0, []
            # Only need to scan ListA
            for i in range(0, length):
                if ListA[i] in visited: continue
                queue, l = [], []
                queue.append(ListA[i])
                l.append(ListA[i])
                visited.add(ListA[i])
                count = 1
                while len(queue) != 0:
                    for k in range(0, len(queue)):
                        book = queue[-1]
                        del queue[-1]
                        # find the next candidates
                        for node in m[book]:
                            if node in visited: continue
                            queue.append(node)
                            visited.add(node)
                            l.append(node)
                            count += 1
                    # collect result
                    if count > max_count:
                        max_count = count
                        res = l
            return res
    
    # s = Solution()
    # print(s.maximumAssociationSet(["abc","abc","abc"], ["bcd","acd","def"]))
    # print(s.maximumAssociationSet(["a","b","d","e","f"], ["b","c","e","g","g"]))