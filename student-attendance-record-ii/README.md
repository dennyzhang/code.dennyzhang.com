# Leetcode: Student Attendance Record II     :BLOG:Medium:


---

Student Attendance Record II  

---

Similar Problems:  
-   [Student Attendance Record I](https://brain.dennyzhang.com/student-attendance-record-i)
-   [Dynamic Programming Problems](https://brain.dennyzhang.com/review-dynamicprogramming), Tag: [#dynamicprogramming](https://brain.dennyzhang.com/tag/dynamicprogramming)

---

Given a positive integer n, return the number of all possible attendance records with length n, which will be regarded as rewardable. The answer may be very large, return it after mod 109 + 7.  

A student attendance record is a string that only contains the following three characters:  

1.  'A' : Absent.
2.  'L' : Late.
3.  'P' : Present.

A record is regarded as rewardable if it doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).  

Example 1:  

    Input: n = 2
    Output: 8 
    Explanation:
    There are 8 records with length 2 will be regarded as rewardable:
    "PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
    Only "AA" won't be regarded as rewardable owing to more than one absent times.

Note: The value of n won't exceed 100,000.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/student-attendance-record-ii)  

Credits To: [leetcode.com](https://leetcode.com/problems/student-attendance-record-ii/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/student-attendance-record-ii
    ## Basic Ideas: Dynamic Programming
    ##      a0l0, a0l1, a0l2
    ##      a1l0, a1l1, a1l2
    ## Complexity: Time O(n), Space O(1)
    class Solution:
        def checkRecord(self, n):
            """
            :type n: int
            :rtype: int
            """
            if n == 1: return 3
            l = [1, 1, 0, 1, 0, 0]
            for i in range(2, n+1):
                l2 = [None]*6
                # a0l0: first value is P
                l2[0] = l[0]
                # a0l1: first value is P or L
                l2[1] = l[1] + l[0]
                # a0l2: first value is P or L
                l2[2] = l[2] + l[1]
                # a1l0: first value is A or P
                l2[3] = l[0] + l[3]
                # a1l1: first value is A or P or L
                l2[4] = l[1] + l[4] + l[3]
                # a1l2: first value is A or P or L
                l2[5] = l[2] + l[5] + l[4]
                l = l2
            return sum(l)