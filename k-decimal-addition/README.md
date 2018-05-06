# LintCode: K Decimal Addition     :BLOG:Basic:


---

K Decimal Addition  

---

Similar Problems:  
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
    import (
      "strconv"
      "strings")
    func addition (k int, a string, b string) string {
        i, j, carry := len(a)-1, len(b)-1, 0
        res := ""
        for i>=0 && j>=0 {
            v1, _ := strconv.Atoi(string(a[i]))
            v2, _ := strconv.Atoi(string(b[j]))
            v := v1+v2+carry
            if v>=k {
                carry = 1
                v -= k
            } else {
                carry = 0
            }
            res = strconv.Itoa(v) + res
            i, j = i-1, j-1
        }
        num := ""
        if i>=0 { num = a[0:i+1] }
        if j>=0 { num = b[0:j+1] }
        for i:=len(num)-1; i>=0; i--{
          v, _ := strconv.Atoi(string(num[i]))
          v = v + carry
          if v >=k {
            carry = 1
            v -= k
          } else {
            carry = 0
          }
          res = strconv.Itoa(v) + res
        }
      if carry == 1 {
        res = "1" + res
      }
      res = strings.TrimLeft(res, "0")
      return res
    }