# Leetcode: House Robber III     :BLOG:Hard:


---

Crime activities of House Robbers.  

---

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.  

Determine the maximum amount of money the thief can rob tonight without alerting the police.  

    Example 1:
         3
        / \
       2   3
        \   \ 
         3   1
    Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

    Example 2:
         3
        / \
       4   5
      / \   \ 
     1   3   1
    Maximum amount of money the thief can rob = 4 + 5 = 9.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/house-robber-iii)  

Credits To: [Leetcode.com](https://leetcode.com/problems/house-robber-iii/description/)  

Leave me comments, if you know how to solve.  

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