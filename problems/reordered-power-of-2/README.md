
# Leetcode: Reordered Power of 2     :BLOG:Medium:

---

Reordered Power of 2  

---

Similar Problems:  

-   Tag: [#inspiring](https://code.dennyzhang.com/tag/inspiring)

---

Starting with a positive integer N, we reorder the digits in any order (including the original order) such that the leading digit is not zero.  

Return true if and only if we can do this in a way such that the resulting number is a power of 2.  

Example 1:  

    Input: 1
    Output: true

Example 2:  

    Input: 10
    Output: false

Example 3:  

    Input: 16
    Output: true

Example 4:  

    Input: 24
    Output: false

Example 5:  

    Input: 46
    Output: true

Note:  

-   1 <= N <= 10^9

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/reordered-power-of-2)  

Credits To: [leetcode.com](https://leetcode.com/problems/reordered-power-of-2/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution:

    // Blog link: https://code.dennyzhang.com/reordered-power-of-2
    // Basic Ideas:
    // 10^9 ~= 2^30. We only have 30 numbers which is power of 2
    //
    // Complexity: Time O(1), Space O(1)
    import (
        "math"
        "sort"
        "strings"
    )
    
    func reorderedPowerOf2(N int) bool {
        var str, strGood string
        var l []string
        str = strconv.Itoa(N)
        l = strings.Split(str, "")
        sort.Strings(l)
        str = strings.Join(l, "")
        for v:=1; v<=int(math.Pow(10, 9)); v=v*2 {
    	strGood = strconv.Itoa(v)
    	l = strings.Split(strGood, "")
    	sort.Strings(l)
    	strGood = strings.Join(l, "")
    	if str == strGood { return true }
        }
        return false
    }

