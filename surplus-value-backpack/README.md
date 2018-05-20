# LintCode: Surplus Value Backpack     :BLOG:Hard:


---

Surplus Value Backpack  

---

Similar Problems:  
-   Tag: [#linkedlist](https://code.dennyzhang.com/tag/linkedlist)

---

There is a backpack with a capacity of c.  
There are n Class A items, the volume of the i th Class A item is a[i], and the value of the item is the remaining capacity of the backpack after loading the item \* k1.  
There are m Class B items, the volume of the i th Class B item is b[i], and the value of the item is the remaining capacity of the backpack after loading the item \* k2.  
Find the maximum value can be obtained.  

Notice  
-   1 <= k1, k2, c, a[i], b[i] <= 10^7
-   1 <= n, m <= 1000

Example  

    Given k1 = 3,k2 = 2,c = 7,n = 2,m = 3,a = [4,3],b = [1,3,2],return 23.
    
    Explanation:
    2 * (7-1)+2*(6-2) + 3 * (4-3) = 23

    Given k1 = 1,k2 = 2,c = 5,n = 1,m = 1,a = [2],b = [1],return 10.
    
    Explanation:
    2 * (5-1)+1*(4-2) = 10

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/surplus-value-backpack)  

Credits To: [lintcode.com](http://www.lintcode.com/en/problem/surplus-value-backpack/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/surplus-value-backpack
    
    class Solution:
        """
        @param k1: The coefficient of A
        @param k2: The  coefficient of B
        @param c: The volume of backpack
        @param n: The amount of A
        @param m: The amount of B
        @param a: The volume of A
        @param b: The volume of B
        @return: Return the max value you can get
        """
        def getMaxValue(self, k1, k2, c, n, m, a, b):
            # Write your code here