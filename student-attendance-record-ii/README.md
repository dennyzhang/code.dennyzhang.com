# Leetcode: Student Attendance Record II     :BLOG:Hard:


---

Identity number which appears exactly once.  

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

Credits To: [Leetcode.com](https://leetcode.com/problems/student-attendance-record-ii/description/)  

Hint: Time O(n), Space O(1). Moore voting  

Leave me comments, if you know how to solve.  

Useful link: [here](https://discuss.leetcode.com/topic/17564/boyer-moore-majority-vote-algorithm-and-my-elaboration)  

    ## Basic Ideas:
    ##       No more than 2 elements would be qualified.
    ## Complexity: Time O(n), Space O(1)
    ## Sample Data:
    ##    1 2 3 2 3 3
    ## Asummption:
    class Solution(object):
        def majorityElement(self, nums):
            """
            :type nums: List[int]
            :rtype: List[int]
            """
            length = len(nums)
            if length == 0:
                return 
            n1, n2 = None, None
            c1, c2 = 0, 0
            for num in nums:
                if num == n1:
                    c1 += 1
                elif num == n2:
                    c2 += 1
                elif c1 == 0:
                    n1, c1 = num, 1
                elif c2 == 0:
                    n2, c2 = num, 1
                else:
                    c1, c2 = c1 - 1, c2 - 1
            c1, c2 = 0, 0
            for num in nums:
                if num == n1:
                    c1 += 1
                elif num == n2:
                    c2 += 1
            # print("n1: %d, c1: %d, n2: %d, c2: %d. length: %d" % (n1, c1, n2, c2, length))
            res = 
            if c1 > length/3:
                res.append(n1)
            if c2 > length/3:
                res.append(n2)
            return res
    
    s = Solution()
    # print s.majorityElement([1, 2])
    # print s.majorityElement([1,2,1,1,1,3,3,4,3,3,3,4,4,4])
    print s.majorityElement([1,1,1,2,3,4,5,6])
    # print s.majorityElement([1, 2, 3, 2, 3, 3])

More Reading:  
-   [Leetcode: Majority Element](http://brain.dennyzhang.com/majority-element/)