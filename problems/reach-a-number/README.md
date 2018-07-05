# Leetcode: Reach a Number     :BLOG:Medium:


---

Reach a Number  

---

Similar Problems:  
-   [Reaching Points](https://code.dennyzhang.com/reaching-points)
-   [Review: Math Problems](https://code.dennyzhang.com/review-math)
-   Tag: [math](https://code.dennyzhang.com/tag/math)

---

You are standing at position 0 on an infinite number line. There is a goal at position target.  

On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.  

Return the minimum number of steps required to reach the destination.  

Example 1:  

    Input: target = 3
    Output: 2
    Explanation:
    On the first move we step from 0 to 1.
    On the second step we step from 1 to 3.

Example 2:  

    Input: target = 2
    Output: 3
    Explanation:
    On the first move we step from 0 to 1.
    On the second move we step  from 1 to -1.
    On the third move we step from -1 to 2.

Note:  
-   target will be a non-zero integer in the range [-10^9, 10^9].

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/reach-a-number)  

Credits To: [leetcode.com](https://leetcode.com/problems/reach-a-number/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/reach-a-number
    ## Basic Ideas: BFS
    ##      1 - 2 + 3 - 4 + 5 - 6 ... : get -n
    ##      -1 + 2 - 3 + 4 - 5 + 6 ... : get n
    ##
    ##      So the minimum step will be no more than 2n.
    ##      If abs(value) is bigger than 2*n, we don't need to examine it.
    ##
    ## Complexity: Time O(n), Space O(n)
    class Solution:
        def reachNumber(self, target):
            """
            :type target: int
            :rtype: int
            """
            if target == 0: return 0
            import collections
            queue = collections.deque()
            step = 0
            queue.append(0)
            while len(queue) != 0 and step<=abs(2*target):
                step += 1
                for k in range(len(queue)):
                    value = queue.popleft()
                    value2 = value+step
                    if value2 == target: return step
                    queue.append(value2)
    
                    value2 = value-step
                    if value2 == target: return step
                    queue.append(value2)