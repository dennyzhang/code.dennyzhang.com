# Leetcode: Daily Temperatures     :BLOG:Amusing:


---

Daily Temperatures  

---

Similar Problems:  
-   [Leetcode: Leetcode: Next Greater Element I](https://brain.dennyzhang.com/next-greater-element-i)
-   Tag: [#monotonestack](https://brain.dennyzhang.com/tag/monotonestack)

---

Given a list of daily temperatures, produce a list that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.  

For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].  

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/daily-temperatures)  

Credits To: [leetcode.com](https://leetcode.com/problems/daily-temperatures/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/daily-temperatures
    ## Basic Ideas: Monotonous stack can help us find first largest element in O(n) time complexity.
    ##
    ##              Descending stack: find the next bigger nubmer for each element
    ##
    ##              For any given number, if we haven't met the bigger number. We push it to the stack
    ##              If we pop out one element, we do find a bigger number than this element.
    ##
    ## Complexity: Time O(n), Space O(n)
    class Solution(object):
        def dailyTemperatures(self, temperatures):
            """
            :type temperatures: List[int]
            :rtype: List[int]
            """
            length = len(temperatures)
            res = [0]*length
            stack = []
            for i in xrange(length):
                # If current number is bigger, we solved the previous puzzles
                while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:
                    k = stack.pop()
                    # t[i] is the next bigger number than t[k]
                    res[k] = i-k
                stack.append(i)
            return res