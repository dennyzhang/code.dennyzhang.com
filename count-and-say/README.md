
# Leetcode: Count and Say     :BLOG:Basic:

---

Count and Say  

---

The count-and-say sequence is the sequence of integers with the first five terms as following:  

    1.     1
    2.     11
    3.     21
    4.     1211
    5.     111221

    1 is read off as "one 1" or 11.
    11 is read off as "two 1s" or 21.
    21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth term of the count-and-say sequence.  

Note: Each term of the sequence of integers will be represented as a string.  

    Example 1:
    
    Input: 1
    Output: "1"

    Example 2:
    
    Input: 4
    Output: "1211"

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/count-and-say)  

Credits To: [leetcode.com](https://leetcode.com/problems/count-and-say/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/count-and-say
    // Basic Ideas:
    //   From n-1 to n
    //       1.     1
    //       2.     11
    //       3.     21
    //       4.     1211
    //       5.     111221 
    //       6.     312211
    //       7.     13112221
    //       8.     1113213211
    //       9.     31131211131221
    //      10.     13211311123113112211
    // Complexity: Time O(n), Space O(m)
    //    m = length of target string
    func countAndSay(n int) string {
        if n == 1 { return "1" }
        str := "1"
        for i:=1; i<n; i++ {
            str2 := ""
            count := 1
            for i, ch := range str+" " {
                if i == 0 { continue }
                if ch != rune(str[i-1]) {
                    str2 += fmt.Sprintf("%d%s", count, string(str[i-1]))
                    count = 1
                } else {
                    count++
                }
            }
            str = str2
        }
        return str
    }

