# Leetcode: Reverse Bits     :BLOG:Basic:


---

Identity number which appears exactly once.  

---

Reverse bits of a given 32 bits unsigned integer.  

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).  

Follow up:  
If this function is called many times, how would you optimize it?  

Blog link: <http://brain.dennyzhang.com/reverse-bits>  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/reverse-bits)  

Credits To: [leetcode.com](https://leetcode.com/problems/reverse-bits/description)  

Leave me comments, if you know how to solve.  

    class Solution(object):
        def reverseBits(self, n):
            i = 0
            ret = 0
            while i < 32:
                ret = ret << 1
                ret = ret | (n % 2)
                n = n >> 1
                i = i + 1
            return ret