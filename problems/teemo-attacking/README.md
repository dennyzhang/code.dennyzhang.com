
# Leetcode: Teemo Attacking     :BLOG:Medium:

---

Teemo Attacking  

---

Similar Problems:  

-   [Merge Intervals](https://code.dennyzhang.com/merge-intervals)
-   [Review: Interval Problems](https://code.dennyzhang.com/review-interval)
-   Tag: [#interval](https://code.dennyzhang.com/tag/interval), [#game](https://code.dennyzhang.com/tag/game), [#manydetails](https://code.dennyzhang.com/tag/manydetails), [#classic](https://code.dennyzhang.com/tag/classic)

---

In LOL world, there is a hero called Teemo and his attacking can make his enemy Ashe be in poisoned condition. Now, given the Teemo's attacking ascending time series towards Ashe and the poisoning time duration per Teemo's attacking, you need to output the total time that Ashe is in poisoned condition.  

You may assume that Teemo attacks at the very beginning of a specific time point, and makes Ashe be in poisoned condition immediately.  

Example 1:  

    Input: [1,4], 2
    Output: 4
    Explanation: At time point 1, Teemo starts attacking Ashe and makes Ashe be poisoned immediately. 
    This poisoned status will last 2 seconds until the end of time point 2. 
    And at time point 4, Teemo attacks Ashe again, and causes Ashe to be in poisoned status for another 2 seconds. 
    So you finally need to output 4.

Example 2:  

    Input: [1,2], 2
    Output: 3
    Explanation: At time point 1, Teemo starts attacking Ashe and makes Ashe be poisoned. 
    This poisoned status will last 2 seconds until the end of time point 2. 
    However, at the beginning of time point 2, Teemo attacks Ashe again who is already in poisoned status. 
    Since the poisoned status won't add up together, though the second poisoning attack will still work at time point 2, it will stop at the end of time point 3. 
    So you finally need to output 3.

Note:  

1.  You may assume the length of given time series array won't exceed 10000.
2.  You may assume the numbers in the Teemo's attacking time series and his poisoning time duration per attacking are non-negative integers, which won't exceed 10,000,000.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/teemo-attacking)  

Credits To: [leetcode.com](https://leetcode.com/problems/teemo-attacking/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/teemo-attacking
    // Basic Ideas: Merge Intervals
    // Here we choose [start, end), instead of [start, end)
    // Remember to collect the last attack
    //
    // Complexity: Time O(n), Space O(1)
    func findPoisonedDuration(timeSeries []int, duration int) int {
      if len(timeSeries) == 0 { return 0 }
      res := 0
      start, end := timeSeries[0], timeSeries[0]+duration
      for i:=1; i<len(timeSeries); i++ {
        time := timeSeries[i]
        if time <= end {
          // overlapped
          end = time+duration
        } else {
          // not overlapped
          res += end-start
          start, end = time, time+duration
        }
      }
      // collect the last interval
      res += end-start
      return res
    }

