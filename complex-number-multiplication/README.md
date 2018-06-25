# Leetcode: Complex Number Multiplication     :BLOG:Basic:


---

Complex Number Multiplication  

---

Similar Problems:  
-   [Review: Math Problems](https://code.dennyzhang.com/review-math)
-   [Solve the Equation](https://code.dennyzhang.com/solve-the-equation)
-   Tag: [#math](https://code.dennyzhang.com/tag/math)

---

Given two strings representing two complex numbers.  

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.  

Example 1:  

    Input: "1+1i", "1+1i"
    Output: "0+2i"
    Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.

Example 2:  

    Input: "1+-1i", "1+-1i"
    Output: "0+-2i"
    Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.

Note:  

-   The input strings will not have extra blank.
-   The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range of [-100, 100]. And the output should be also in this form.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/complex-number-multiplication)  

Credits To: [leetcode.com](https://leetcode.com/problems/complex-number-multiplication/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/complex-number-multiplication
    // Basic Ideas:
    //      (v1+v2*i) * (v3+v4*i) ->
    //        v1*v3 + (v1*v4+v2*v3)*i + v2*v4*i*i ->
    //        v1*v3-v2*v4 + (v1*v4+v2*v3)*i
    // Complexity: Time O(1), Space O(1)
    func complexNumberMultiply(a string, b string) string {
        v1, v2 := splitExpr(a)
        v3, v4 := splitExpr(b)
        return fmt.Sprintf("%d+%di", v1*v3-v2*v4, v1*v4+v2*v3)
    }
    
    func splitExpr(a string) (v1, v2 int) {
        i := strings.Index(a, "+")
        v1, _ = strconv.Atoi(a[0:i])
        v2, _ = strconv.Atoi(a[i+1:len(a)-1])
        return
    }