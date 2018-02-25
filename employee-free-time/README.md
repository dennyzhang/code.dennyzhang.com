# Leetcode: Employee Free Time     :BLOG:Hard:


---

Identity Employee Free Time  

---

Similar Problems:  
-   [Review: Interval Problems](https://brain.dennyzhang.com/review-interval)

---

We are given a list schedule of employees, which represents the working time for each employee.  

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.  

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.  

    Example 1:
    Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
    Output: [[3,4]]
    Explanation:
    There are a total of three employees, and all common
    free time intervals would be [-inf, 1], [3, 4], [10, inf].
    We discard any intervals that contain inf as they aren't finite.

    Example 2:
    Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
    Output: [[5,6],[7,9]]

    (Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined.)
    
    Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

Note:  
1.  schedule and schedule[i] are lists with lengths in range [1, 50].
2.  0 <= schedule[i].start < schedule[i].end <= 10^8.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/employee-free-time)  

Credits To: [leetcode.com](https://leetcode.com/problems/employee-free-time/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/employee-free-time
    # Definition for an interval.
    # class Interval(object):
    #     def __init__(self, s=0, e=0):
    #         self.start = s
    #         self.end = e
    
    class Solution(object):
        def employeeFreeTime(self, schedule):
            """
            :type schedule: List[List[Interval]]
            :rtype: List[Interval]
            """