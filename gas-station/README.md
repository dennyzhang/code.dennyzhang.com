# Leetcode: Gas Station     :BLOG:Hard:


---

Gas Station  

---

Similar Problems:  
-   [Review: Greedy Problems](https://brain.dennyzhang.com/review-greedy), [Tag: #greedy](https://brain.dennyzhang.com/tag/greedy)

---

There are N gas stations along a circular route, where the amount of gas at station i is gas[i].  

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.  

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.  

Note:  
The solution is guaranteed to be unique.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/gas-station)  

Credits To: [leetcode.com](https://leetcode.com/problems/gas-station/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/gas-station
    ## Basic Ideas: One pass
    ##    If gas[i] - cost[i] < 0, this node can't be the target
    ##
    ##    If total sum of gas-cost < 0, we can't find the solution.
    ##    If total sum of gas-cost >=0, we must be able to find one solution
    ##
    ##    Get accumulated sum of gas-cost
    ##       If it turn to negative, this node and all previous nodes can't be the target
    ##
    ##    Question: 
    ##       How to handle a circle, instead of an array?
    ##       How to detect cases with no solution?
    ##
    ## Complexity: Time O(n), Space O(1)
    class Solution:
        def canCompleteCircuit(self, gas, cost):
            """
            :type gas: List[int]
            :type cost: List[int]
            :rtype: int
            """
            length = len(gas)
            res, curSum, totalSum = 0, 0, 0
            for i in range(0, length):
                totalSum += gas[i] - cost[i]
                curSum += gas[i] - cost[i]
                if curSum < 0:
                    res = i+1
                    curSum = 0
    
            return res if totalSum >=0 else -1