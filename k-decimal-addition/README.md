# LintCode: K Decimal Addition     :BLOG:Basic:


---

K Decimal Addition  

---

Similar Problems:  
-   [Add Strings](https://code.dennyzhang.com/add-strings)
-   [Additive Number](https://code.dennyzhang.com/additive-number)
-   Tag: [#classic](https://code.dennyzhang.com/tag/classic)

---

Give k, a, b, which means a and b are all k base numbers, and output a + b.  

Example  

    Given k = 3, a = "12", b = "1", return "20".
    
    Explanation:
    12 + 1 = 20 in 3 bases.

    Given k = 10, a = "12", b = "1", return "13".
    
    Explanation:
    12 + 1 = 13 in 10 bases.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/k-decimal-addition)  

Credits To: [lintcode.com](https://www.lintcode.com/problem/k-decimal-addition/description)  

Leave me comments, if you have better ways to solve.  

    // Blog link: https://code.dennyzhang.com/k-decimal-addition
    // Basic Ideas:
    // Complexity: Time O(n), Space O(n)
    import ("strconv"
           "strings")
    func addition (k int, a string, b string) string {
        carry, res := 0, ""
        for i, j := len(a)-1, len(b)-1; 
            i>=0 || j>=0 || carry !=0;
            i, j = i-1, j-1 {
            v1, v2 := 0, 0
            if i>=0 { v1, _ = strconv.Atoi(string(a[i])) }
            if j>=0 { v2, _ = strconv.Atoi(string(b[j])) }
            v := v1+v2+carry
            if v>=k {
                carry = 1
                v -= k
            } else {
                carry = 0
            }
            res = strconv.Itoa(v) + res
        }
      return strings.TrimLeft(res, "0")
    }