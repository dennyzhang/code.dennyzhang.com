# Leetcode: Monotone Increasing Digits     :BLOG:Basic:


---

Monotone Increasing Digits  

---

Similar Problems:  
-   Tag: [#monotonestack](https://brain.dennyzhang.com/tag/monotonestack)

---

Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.  

(Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.)  

Example 1:  

    Input: N = 10
    Output: 9

Example 2:  

    Input: N = 1234
    Output: 1234

Example 3:  

    Input: N = 332
    Output: 299

Note: N is an integer in the range [0, 10^9].  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/monotone-increasing-digits)  

Credits To: [leetcode.com](https://leetcode.com/problems/monotone-increasing-digits/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/monotone-increasing-digits
    ## Basic Ideas: monotone stack
    ##   Let's say we found one digit in the following digit which is smaller than current digit.
    ##   We decrease current digit by 1, then change the following to '9'   
    ##
    ## Sample Data:
    ##     2342
    ##     2<3, so we get 2299
    ## Complexity:
    class Solution(object):
        def monotoneIncreasingDigits(self, N):
            """
            :type N: int
            :rtype: int
            """
            l = list(str(N))
            length = len(l)
            for i in range(length): l[i] = ord(l[i]) - ord('0')
    
            # monotone stack: find the next smaller value
            stack = []
            state = [-1]*length
            for i in range(length):
                # current digit is smaller than the previous one
                while len(stack) and l[i] < l[stack[-1]]:
                    k = stack.pop(-1)
                    state[k] = i
                stack.append(i)
    
            # make the change
            for i in range(length-1, -1, -1):
                if state[i] != -1:
                    l[i] -= 1
                    for j in range(i+1, length): l[j] = 9
                    break
            # get the result
            res = 0
            for i in range(length): res = res*10+l[i]
            return res
    
    s = Solution()
    print(s.monotoneIncreasingDigits(120)) # 119
    print(s.monotoneIncreasingDigits(332)) # 299