# Leetcode: Integer to Roman     :BLOG:Basic:


---

Integer to Roman  

---

Similar Problems:  
-   [Integer to English Words](https://code.dennyzhang.com/integer-to-english-words)
-   [Roman to Integer](https://code.dennyzhang.com/roman-to-integer)
-   Tag: [#math](https://code.dennyzhang.com/tag/math)

---

Given an integer, convert it to a roman numeral.  

Input is guaranteed to be within the range from 1 to 3999.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/integer-to-roman)  

Credits To: [leetcode.com](https://leetcode.com/problems/integer-to-roman/description/)  

Leave me comments, if you have better ways to solve.  

    // Blog link: https://code.dennyzhang.com/integer-to-roman
    // Basic Ideas:
    //    Symbol  I  V  X   L   C     D    M
    //    Value   1  5  10  50  100  500  1,000
    //  From 3998 -> 
    //       3000 -> MMM
    //        900 -> DCCC
    //        90 ->  LXXXX
    //        8  -> VIII
    //      
    // Complexity: Time O(1), Space O(1)
    func intToRoman(num int) string {
        thousands := []string {"", "M", "MM", "MMM"}
        hundreds := []string {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"}
        tens := []string {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX","LXXX", "XC"}
        digits := []string {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII","IX"}
        var res bytes.Buffer
        res.WriteString(thousands[num/1000])
        res.WriteString(hundreds[num%1000/100])
        res.WriteString(tens[num%100/10])
        res.WriteString(digits[num%10])
        return res.String()
    }