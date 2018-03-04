# Leetcode: Convert a Number to Hexadecimal     :BLOG:Basic:


---

Convert a Number to Hexadecimal  

---

Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two's complement method is used.  

Note:  

1.  All letters in hexadecimal (a-f) must be in lowercase.
2.  The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
3.  The given number is guaranteed to fit within the range of a 32-bit signed integer.
4.  You must not use any method provided by the library which converts/formats the number to hex directly.

    Example 1:
    
    Input:
    26
    
    Output:
    "1a"

    Example 2:
    
    Input:
    -1
    
    Output:
    "ffffffff"

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/convert-a-number-to-hexadecimal)  

Credits To: [leetcode.com](https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/convert-a-number-to-hexadecimal
    ## Basic Ideas: For negative numbers, two's complement
    ##        https://en.wikipedia.org/wiki/Two%27s_complement
    ##        -1 ---> pow(2, 32) + 1
    ## Complexity: Time O(k), Space O(1). k = len(result)
    class Solution:
        def toHex(self, num):
            """
            :type num: int
            :rtype: str
            """
            if num == 0: return '0'
            if num < 0: return self.toHex(pow(2, 32)+num)
            res = ''
            while num != 0:
                mod_val = num%16
                num = int(num/16)
                if mod_val < 10:
                    mod_str = str(mod_val)
                else:
                    mod_str = chr(ord('a') + mod_val-10)
                # print(mod_val, mod_str)
                res = '%s%s' % (mod_str, res)
            return res
    
    # s = Solution()
    # print(s.toHex(-1)) # ffffffff
    # print(s.toHex(26)) # 1a