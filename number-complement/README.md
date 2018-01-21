# Leetcode: Number Complement     :BLOG:Basic:


---

Number Complement  

---

Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.  

Note:  
The given integer is guaranteed to fit within the range of a 32-bit signed integer.  
You could assume no leading zero bit in the integer's binary representation.  

    Example 1:
    Input: 5
    Output: 2
    Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

    Example 2:
    Input: 1
    Output: 0
    Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/number-complement)  

Credits To: [leetcode.com](https://leetcode.com/problems/number-complement/description/)  

Leave me comments, if you know how to solve.  

    class Solution(object):
        def findComplement(self, num):
            """
            :type num: int
            :rtype: int
            """
            i = num
            ret = 0
            digit_count = 0
    
            while i != 0:
                reverse_current_digit = 1 ^ (i % 2)
                ret = (reverse_current_digit << digit_count) | ret
                digit_count = digit_count + 1
                i = i >> 1
                # print("i: %i, ret: %d, digit_count: %d, reverse_current_digit: %d", i, ret, digit_count, reverse_current_digit)
    
            return ret
    if __name__ == '__main__':
        s = Solution()
        print s.findComplement(5) # 2
        print s.findComplement(3) # 0
        print s.findComplement(1) # 0