# Leetcode: Divide Two Integers     :BLOG:Amusing:


---

Divide two integers without using multiplication, division and mod operator.  

---

Divide two integers without using multiplication, division and mod operator.  

If it is overflow, return MAX\_INT.  

Blog link: <http://brain.dennyzhang.com/divide-two-integers>  

Github: challenges-leetcode-interesting  

Credits To: leetcode.com  

Leave me comments, if you know how to solve.  

    ## Basic Ideas: generate a list of [1, 2, 4, 8, 16...] and [d, 2d, 4d, 8d, ...]
    ## Complexity: Time O(log(n)), Space O(log(n))
    ## Sample Data: 
    ##     divide(124, 41)
    ##     divide(124, 0)
    ##     divide(123, -1)
    class Solution(object):
        def divide(self, dividend, divisor):
            """
            :type dividend: int
            :type divisor: int
            :rtype: int
            """
            ## Idea:
            ## Complexity: Time O(log(n)), Space O(1)
            ## Sample Data:
            ##     divide(124, 41)
            ##     divide(124, 0)
            ##     divide(123, -1)
            max_int = 2147483647
            if divisor == 0:
                return max_int
            is_positive = (dividend<0) is (divisor<0)
            dividend, divisor = abs(dividend), abs(divisor)
    
            pow2_value = 1
            powd_value = divisor
            while dividend > powd_value:
                pow2_value <<= 1
                powd_value <<= 1
    
            res = 0
            while dividend > 0 and pow2_value > 0:
                if dividend >= powd_value:
                    dividend = dividend - powd_value
                    res += pow2_value
                powd_value >>= 1
                pow2_value >>= 1
    
            if is_positive is False:
                res = -res
    
            # overflow case: -(min)/-1
            if res > max_int:
                res = max_int
            return res
    
        def divide_v1(self, dividend, divisor):
            """
            :type dividend: int
            :type divisor: int
            :rtype: int
            """
            max_int = 2147483647
            min_negative = -2147483648
            pow2_list, powd_list = [], []
            if divisor == 0:
                return max_int
    
            is_positive = (dividend<0) is (divisor<0)
            dividend, divisor = abs(dividend), abs(divisor)
    
            res = 0
            pow2_list.append(1)
            powd_list.append(divisor)
            while dividend > powd_list[-1]:
                pow2_list.append(pow2_list[-1]+pow2_list[-1])
                powd_list.append(powd_list[-1]+powd_list[-1])
    
            res = 0
            i = len(powd_list)-1
            while dividend>0 and i>-1:
                if powd_list[i] <= dividend:
                    res += pow2_list[i]
                    dividend -= powd_list[i]
                i -= 1
    
            if is_positive is False:
                res = -res
    
            return min(max(min_negative, res), max_int)