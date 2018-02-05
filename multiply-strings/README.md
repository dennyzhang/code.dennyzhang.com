# Leetcode: Multiply Strings     :BLOG:Medium:


---

Multiply Strings  

---

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.  

Note:  

1.  The length of both num1 and num2 is < 110.
2.  Both num1 and num2 contains only digits 0-9.
3.  Both num1 and num2 does not contain any leading zero.
4.  You must **not use any built-in BigInteger library or convert the inputs to integer** directly.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/multiply-strings)  

Credits To: [leetcode.com](https://leetcode.com/problems/multiply-strings/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/multiply-strings
    ## Basic Ideas:
    ##
    ## Complexity:
    class Solution:
        def multiply(self, num1, num2):
            """
            :type num1: str
            :type num2: str
            :rtype: str
            """
            max_length = len(num1) + len(num2) + 1
            res = [0]*max_length
            digit_count = 0
            for ch1 in num1[::-1]:
                v1 = ord(ch1) - ord('0')
                # get row value
                row_value = 
                carry = 0
                for ch2 in num2[::-1]:
                    v2 = ord(ch2) - ord('0')
                    row_value.append((v1*v2+carry)%10)
                    carry = int((v1*v2+carry)/10)
                if carry != 0: row_value.append(carry)
    
                for k in range(0, digit_count):
                    row_value.insert(0, 0)
                digit_count += 1
    
                # add rowValue into res
                # print(max_length, res, row_value)
                carry = 0
                for i in range(0, len(row_value)+1):
                    if i == len(row_value):
                        if carry!=0: res[i] = carry
                        continue
                    new_carry = int((res[i]+row_value[i]+carry)/10)
                    res[i] = (res[i]+row_value[i]+carry)%10
                    carry = new_carry
    
            # get the final result
            while res[-1] == 0 and len(res) != 1: del res[-1]
            for i in range(0, len(res)):
                res[i] = chr(res[i] + ord('0'))
            return ''.join(res)[::-1]
    
    s = Solution()
    print(s.multiply("123", "45")) # 5535
    print(s.multiply("45", "123")) # 5535