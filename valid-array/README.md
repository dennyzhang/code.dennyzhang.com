# LintCode: Valid Array     :BLOG:Basic:


---

Valid Array  

---

Similar Problems:  
-   Tag: [#hashmap](https://code.dennyzhang.com/tag/hashmap)

---

If an array contains only one number that has an odd number of times, the array is valid, otherwise the array is invalid. Enter an array a containing only positive integers to determine if the array is valid. Return the number which has odd number of times if it is valid, return -1 if it is invalid.  

The length of the array does not exceed 10^5​, each number in the array is less than or equal to 10^9.  

Example  

    Given a=[1,1,2,2,3,4,4,5,5], return 3.
    
    Explanation:
    In this array, only 3 has odd number of times, so return 3.

    Given a=[1,1,2,2,3,4,4,5], return -1.
    
    Explanation:
    In this array, 3 and 5 have odd number of times, so it is invalid and return -1.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/valid-array)  

Credits To: [lintcode.com](https://www.lintcode.com/problem/valid-array/description)  

Leave me comments, if you have better ways to solve.  

---

-   Solution: hasmap

    // Blog link: https://code.dennyzhang.com/valid-array
    // Basic Ideas: hashmap
    // Complexity: Time O(n), Space O(n)
    /**
     * @param a: The array.
     * @return: The number which has odd number of times or -1.
     */
    func isValid (a []int) int {
        m := map[int]int{}
        for _, num := range a {
            m[num] += 1
            if m[num] % 2 == 0 { delete(m, num) }
        }
        res := -1
        if len(m) == 1 { 
            for k := range m {
                res = k
                break
            }
        }
        return res
    }