# Leetcode: Add Strings     :BLOG:Basic:


---

Add 2 strings of big numbers  

---

Similar Problems:  
-   [LintCode: K Decimal Addition](https://code.dennyzhang.com/k-decimal-addition)
-   [Additive Number](https://code.dennyzhang.com/additive-number)

---

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.  

Note:  

The length of both num1 and num2 is < 5100.  
Both num1 and num2 contains only digits 0-9.  
Both num1 and num2 does not contain any leading zero.  
You must not use any built-in BigInteger library or convert the inputs to integer directly.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/add-strings)  

Credits To: [leetcode.com](https://leetcode.com/problems/add-strings/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/add-strings
    // Basic Ideas: 
    //  Handle carry
    //  Only stop when both strings have finished
    // Complexity: Time O(n), Space O(n)
    import "strconv"
    func addStrings(num1 string, num2 string) string {
        carry, res := 0, ""
        for i, j:= len(num1)-1, len(num2)-1;
            i>=0 || j>=0 || carry!=0; 
            i, j = i-1, j-1 {
            v1, v2, v := 0, 0, 0
            if i>=0 { v1, _ = strconv.Atoi(string(num1[i])) }
            if j>=0 { v2, _ = strconv.Atoi(string(num2[j])) }
            v = v1+v2+carry
            if v>=10 {
                carry = 1
                v -= 10
            } else {
                carry = 0
            }
            res = strconv.Itoa(v)+res
        }
        return res
    }