# Leetcode: Largest Number     :BLOG:Medium:


---

Given a list of non negative integers, arrange them such that they form the largest number.  

---

Similar Problems:  
-   [Review: Problems With Many Details](https://code.dennyzhang.com/review-manydetails)
-   Tag: [#manydetails](https://code.dennyzhang.com/tag/manydetails)

---

Given a list of non negative integers, arrange them such that they form the largest number.  

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.  

Note: The result may be very large, so you need to return a string instead of an integer.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/largest-number)  

Credits To: [leetcode.com](https://leetcode.com/problems/largest-number/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/largest-number
    ## Basic Ideas: Quick sort list with customized compare logic. Then Concat them as one.
    ##             "9" vs "30"
    ##             "34" vs "3"
    ##             "3012" vs "30"
    ##             "121" vs "12
    ##             "128" vs "12"
    ## Complexity: Time O(n*log(n)) length of integer is short, Space O(n)
    class Solution:
        # @param {integer[]} nums
        # @return {string}
        def largestNumber(self, nums):
            # https://docs.python.org/3/howto/sorting.html
            sorted_nums = sorted(nums, cmp=self.myCompare)
            # print sorted_nums
            res = ""
            for num in sorted_nums:
                res = "%s%s" % (res, str(num))
            # remove leading "0"
            res = res.lstrip('0')
            if res == '':
                res = '0'
            return res
    
        def myCompare(self, v1, v2):
            # print("myCompare. v1: %d, v2: %d" % (v1, v2))
            s1 = str(v1)
            s2 = str(v2)
            if s1+s2 == s2+s1:
                return 0
            if s1+s2 > s2+s1:
                return -1
            else:
                return 1
    
    # s = Solution()
    # print s.largestNumber([3, 34, 30, 5, 9]) # 9533430
    # print s.largestNumber([128, 12]) #12812
    # print s.largestNumber([121,12]) #12121