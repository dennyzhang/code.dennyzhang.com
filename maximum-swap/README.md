# Leetcode: Maximum Swap     :BLOG:Medium:


---

Maximum Swap  

---

Similar Problems:  

-   [Swap Adjacent in LR String](https://brain.dennyzhang.com/swap-adjacent-in-lr-string)
-   [Global and Local Inversions](https://brain.dennyzhang.com/global-and-local-inversions)
-   Tag: [#linkedlist](https://brain.dennyzhang.com/tag/linkedlist)

---

Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.  

Example 1:  

    Input: 2736
    Output: 7236
    Explanation: Swap the number 2 and the number 7.

Example 2:  

    Input: 9973
    Output: 9973
    Explanation: No swap.

Note:  
The given number is in the range [0, 108]  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/maximum-swap)  

Credits To: [leetcode.com](https://leetcode.com/problems/maximum-swap/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/maximum-swap
    ## Basic Ideas: counter with [0, 1, 2, ... 9]
    ##
    ## Complexity: Time O(n), Space O(1)
    class Solution:
        def maximumSwap(self, num):
            """
            :type num: int
            :rtype: int
            """
            res = num
            num_list = list(str(num))
            d = [0]*10
            for ch in num_list: d[int(ch)] += 1
    
            for i in range(len(num_list)):
                v1 = int(num_list[i])
                d[v1] -= 1
                v2 = -1
                for k in range(9, v1, -1):
                    # detect the target
                    if d[k] != 0:
                        v2 = k
                        break
                # from right to left, find v2 then switch
                if v2 != -1:
                    for j in range(len(num_list)-1, i, -1):
                        if int(num_list[j]) == v2:
                            num_list[i], num_list[j] = num_list[j], num_list[i]
                            res = int(''.join(num_list))
                            return res
            return res
    
    s = Solution()    
    print(s.maximumSwap(2736))