# LintCode: Prime Product     :BLOG:Basic:


---

Prime Product  

---

Similar Problems:  
-   [Review: Combinations and Permutations Problems](https://code.dennyzhang.com/review-combination)
-   Tag: [#combination](https://code.dennyzhang.com/tag/combination)

---

Given a non-repeating prime array arr, and each prime number is used at most once, find all the product without duplicate and sort them from small to large.  

Notice  
-   2 <= |arr| <= 9
-   2 <= arr[i] <= 23

Example  

    Given arr = [2,3], return [6].
    
    Explanation:
    2 * 3 = 6.

    Gven arr = [2,3,5], return [6,10,15,30].
    
    Explanation:
    2 * 3 = 6, 2 * 5 = 10, 3 * 5 = 15, 2 * 3 *5 = 30

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/prime-product)  

Credits To: [leetcode.com](https://leetcode.com/problems/prime-product/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/prime-product
    class Solution:
        """
        @param arr: The prime array
        @return: Return the array of all of prime product
        """
        def getPrimeProduct(self, arr):
            ## Basic Ideas: BFS
            ## Complexity: Time O(1), Space O(1)
            arr.sort()
            # 2, 3, 5, 7
            #    23, 25, 27; 35, 37
            #    235, 237; 257; 357
            import collections
            queue = collections.deque()
            for i, num in enumerate(arr):
                if i == len(arr)-1: continue
                queue.append((num, i))
    
            res = []
            while len(queue) != 0:
                for i in range(len(queue)):
                    (num, index) = queue.popleft()
                    for j in range(index+1, len(arr)):
                        queue.append((num*arr[j], j))
                        res.append(num*arr[j])
            return sorted(res)