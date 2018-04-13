# Leetcode: Remove Invalid Parentheses     :BLOG:Hard:


---

Remove Invalid Parentheses  

---

Similar Problems:  
-   [Review: Linked List Problems](https://code.dennyzhang.com/review-linkedlist), [Tag: #linkedlist](https://code.dennyzhang.com/tag/linkedlist)

---

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.  

Note: The input string may contain letters other than the parentheses ( and ).  

Examples:  

    "()())()" -> ["()()()", "(())()"]
    "(a)())()" -> ["(a)()()", "(a())()"]
    ")(" -> [""]

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/remove-invalid-parentheses)  

Credits To: [leetcode.com](https://leetcode.com/problems/remove-invalid-parentheses/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/remove-invalid-parentheses
    ## Basic Ideas: BFS
    ##
    ##   Start with s (removed the trailing '(')
    ##   Find the neighbors: delete one )
    ##
    ##   Assumption:
    ##         ()())a((: ()()a
    ##         aabb: aabb
    ##         x(: x
    ##
    ## Complexity: Time O(pow(2, n)*n), Space O(pow(2, n))
    class Solution:
        def removeInvalidParentheses(self, s):
            """
            :type s: str
            :rtype: List[str]
            """
            index = -1
            for i in range(len(s)-1, -1, -1):
                if s[i] == '(': index = i
                if s[i] == ')': break
            if index != -1: s = s[0:index]
            if self.isValid(s): return [s]
            import collections
            queue = collections.deque()
            seen = set([])
    
            queue.append(s)
            seen.add(s)
    
            should_break = False
            res = set([])
            while len(queue) != 0:
                for i in range(len(queue)):
                    item = queue.popleft()
                    for i in range(len(item)):
                        item2 = item[0:i]+item[i+1:]
                        if item[i] == ')':
                            if self.isValid(item2):
                                should_break = True
                                res.add(item2)
                            else:
                                if item2 not in seen:
                                    queue.append(item2)
                                    seen.add(s)
    
                if should_break: break
            return list(res)
    
        def isValid(self, s):
            left_count = 0
            for ch in s:
                if ch == '(': left_count += 1
                if ch == ')':
                    if left_count == 0: return False
                    left_count -= 1
            return left_count == 0
    
    # s = Solution()
    # print(s.removeInvalidParentheses("x("))