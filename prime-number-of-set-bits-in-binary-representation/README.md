# Leetcode: Prime Number of Set Bits in Binary Representation     :BLOG:Basic:


---

Prime Number of Set Bits in Binary Representation  

---

Given two integers L and R, find the count of numbers in the range [L, R] (inclusive) having a prime number of set bits in their binary representation.  

(Recall that the number of set bits an integer has is the number of 1s present when written in binary. For example, 21 written in binary is 10101 which has 3 set bits. Also, 1 is not a prime.)  

    Example 1:
    
    Input: L = 6, R = 10
    Output: 4
    Explanation:
    6 -> 110 (2 set bits, 2 is prime)
    7 -> 111 (3 set bits, 3 is prime)
    9 -> 1001 (2 set bits , 2 is prime)
    10->1010 (2 set bits , 2 is prime)

    Example 2:
    
    Input: L = 10, R = 15
    Output: 5
    Explanation:
    10 -> 1010 (2 set bits, 2 is prime)
    11 -> 1011 (3 set bits, 3 is prime)
    12 -> 1100 (2 set bits, 2 is prime)
    13 -> 1101 (3 set bits, 3 is prime)
    14 -> 1110 (3 set bits, 3 is prime)
    15 -> 1111 (4 set bits, 4 is not prime)

Note:  

1.  L, R will be integers L <= R in the range [1, 10^6].
2.  R - L will be at most 10000.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/prime-number-of-set-bits-in-binary-representation)  

Credits To: [leetcode.com](https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description/)  

Leave me comments, if you know how to solve.  

    ## Blog link: http://brain.dennyzhang.com/prime-number-of-set-bits-in-binary-representation
    ## Basic Ideas: max(L, R) <= 10^6. The count of bit will be smaller than 1+6*log2(10) = 20
    ##         The possible prime list is: [2, 3, 5, 7, 11, 13, 17, 19]
    ##
    ## Complexity: Time O(n), Space O(1)
    ##             Why the time complexity is O(n)? We do have counted '1' for each number.
    ##             It's because the count of bits is less than 20. So O(20n) = O(n)
    ##
    class Solution(object):
        def countPrimeSetBits(self, L, R):
            """
            :type L: int
            :type R: int
            :rtype: int
            """
            prime_list = [2, 3, 5, 7, 11, 13, 17, 19]
            count = 0
            for n in range(L, R+1):
                if bin(n).count('1') in prime_list:
                    count += 1
    
            return count