
# Leetcode: Random Pick with Blacklist     :BLOG:Hard:

---

Random Pick with Blacklist  

---

Similar Problems:  

-   [Leetcode: Implement Rand10() Using Rand7()](https://code.dennyzhang.com/implement-rand10-using-rand7)
-   Tag: [#random](https://code.dennyzhang.com/tag/random)

---

Given a blacklist B containing unique integers from [0, N), write a function to return a uniform random integer from [0, N) which is NOT in B.  

Optimize it such that it minimizes the call to system's Math.random().  

Note:  

1.  1 <= N <= 1000000000
2.  0 <= B.length < min(100000, N)
3.  [0, N) does NOT include N. See interval notation.

Example 1:  

    Input: 
    ["Solution","pick","pick","pick"]
    [[1,[]],[],[],[]]
    Output: [null,0,0,0]

Example 2:  

    Input: 
    ["Solution","pick","pick","pick"]
    [[2,[]],[],[],[]]
    Output: [null,1,1,1]

Example 3:  

    Input: 
    ["Solution","pick","pick","pick"]
    [[3,[1]],[],[],[]]
    Output: [null,0,0,2]

Example 4:  

    Input: 
    ["Solution","pick","pick","pick"]
    [[4,[2]],[],[],[]]
    Output: [null,1,3,1]
    Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has two arguments, N and the blacklist B. pick has no arguments. Arguments are always wrapped with a list, even if there aren't any.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/random-pick-with-blacklist)  

Credits To: [leetcode.com](https://leetcode.com/problems/random-pick-with-blacklist/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution: XXX

**General Thinkings:**  

    

**Key Observations:**  

    

**Walk Through Testdata**  

    

    // Blog link: https://code.dennyzhang.com/random-pick-with-blacklist

