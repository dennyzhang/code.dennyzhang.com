# Leetcode: Super Pow     :BLOG:Amusing:


---

Super Pow  

---

Similar Problems:  
-   [Pow(x, n)](https://brain.dennyzhang.com/powx-n)
-   Tag: [#recursive](https://brain.dennyzhang.com/tag/recursive)
-   [Review: Math Problems,](https://brain.dennyzhang.com/review-math) Tag: [math](https://brain.dennyzhang.com/tag/math)
-   [Review: Game Problems](https://brain.dennyzhang.com/review-game), [Tag: #game](https://brain.dennyzhang.com/tag/game)

---

Your task is to calculate a^b mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.  

    Example1:
    
    a = 2
    b = [3]
    
    Result: 8

    Example2:
    
    a = 2
    b = [1,0]
    
    Result: 1024

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/super-pow)  

Credits To: [leetcode.com](https://leetcode.com/problems/super-pow/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/super-pow
    ## Basic Ideas:
    ##     (2^120)%k == (((2^12)%k)^10)%k
    ## Complexity: Time O(n), Space O(1). n = len(b)
    class Solution:
        def superPow(self, a, b):
            """
            :type a: int
            :type b: List[int]
            :rtype: int
            """
            length = len(b)
            if length == 0: return 1
            if length == 1: return pow(a, b[0]) % 1337
            v1 = self.superPow(a, b[:-1]) % 1337
            v1 = pow(v1, 10) % 1337
            v2 = self.superPow(a, [b[-1]])
            return (v1*v2)%1337