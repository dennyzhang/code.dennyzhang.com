# LintCode: Deliver The Message     :BLOG:Basic:


---

Deliver The Message  

---

Similar Problems:  
-   [Review: BFS Problems](https://code.dennyzhang.com/review-bfs)
-   Tag: [#bfs](https://code.dennyzhang.com/tag/bfs)

---

Given the information of a company's personnel. The time spent by the ith person passing the message is t[i] and the list of subordinates is list[i]. When someone receives a message, he will immediately pass it on to all his subordinates. Person numbered 0 is the CEO. Now that the CEO has posted a message, find how much time it takes for everyone in the company to receive the message?  

Notice  
-   The number of employees is n,n <= 1000.
-   Everyone can have multiple subordinates but only one superior.
-   Time t[i] <= 10000.
-   -1 represent no subordinates.

Example  

    Given t = [1,2,3], list = [[1,2],[-1],[-1]], return 1.
    
    Explanation:
    The news was passed from the CEO, and the time passed to No. 1 and No. 2 was 1. At this time, all the people in the company received the news.

    Given t = [1,2,1,4,5], list = [[1,2],[3,4],[-1],[-1],[-1]], return 3.
    
    Explanation:
    The message was passed from the CEO. The time passed to the No. 1 and No. 2 characters was 1, the time passed to the No. 3 character was 3, and the message passed through 2 to 4 was faster than passing through 1  so the time which is costed for passing to 4 was 2. Finally at the time of 3, everyone received the news.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/deliver-the-message)  

Credits To: [lintcode.com](http://www.lintcode.com/en/problem/deliver-the-message/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/deliver-the-message
    class Solution:
        """
        @param t: the time of each employee to pass a meeage
        @param subordinate: the subordinate of each employee
        @return: the time of the last staff recieve the message
        """
        def deliverMessage(self, t, subordinate):
            ## Basic Ideas: BFS
            ## Complexity: Time O(n), Space O(n)
            if len(t) == 0: return 0
            import collections
            queue = collections.deque()
    
            res = t[0]
            queue.append((0, 0))
            while len(queue) != 0:
                for k in range(len(queue)):
                    (index, weight) = queue.popleft()
                    # find neighbors
                    if subordinate[index] != [-1]:
                        for i in subordinate[index]:
                            res = max(res, weight + t[index])
                            queue.append((i, weight + t[index]))
            return res