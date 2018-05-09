# Leetcode: Integer to English Words     :BLOG:Hard:


---

Integer to English Words  

---

Similar Problems:  
-   [Integer to Roman](https://code.dennyzhang.com/integer-to-roman)
-   [Reconstruct Original Digits from English](https://code.dennyzhang.com/reconstruct-original-digits-from-english)
-   Tag: [#string](https://code.dennyzhang.com/tag/string), [#manydetails](https://code.dennyzhang.com/tag/manydetails)

---

Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.  

For example,  

    123 -> "One Hundred Twenty Three"
    12345 -> "Twelve Thousand Three Hundred Forty Five"
    1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/integer-to-english-words)  

Credits To: [leetcode.com](https://leetcode.com/problems/integer-to-english-words/description/)  

Leave me comments, if you have better ways to solve.  

    // Blog link: https://code.dennyzhang.com/integer-to-english-words
    // Basic Ideas:
    // 1,234,567
    // ... Billion ... Million ... Thousand ...
    // 1,234,567,896
    //
    // Here we don't necessarily need hashmap. List is fine.
    //
    // Watch out:
    //     0
    //    1000,000
    // Complexity:
    import "strings"
    var digitList = []string {"", "One", "Two", "Three",
      "Four", "Five", "Six", "Seven", "Eight", "Nine"}
    
    var twoDigitList = []string {"Ten", "Eleven", "Twelve",
      "Thirteen", "Fourteen", "Fifteen", 
      "Sixteen", "Seventeen", "Eighteen", "Nineteen"}
    
    var tenList = []string {"Twenty", "Thirty",
      "Forty", "Fifty", "Sixty",
      "Seventy", "Eighty", "Ninety"}
    
    func sectionToWords(num int) string {
      res := ""
      if num >= 100 {
        digit := int(num/100)
        num = num%100
        res = fmt.Sprintf("%s Hundred", digitList[digit])
      }
      if num >= 20 {
        digit := int(num/10)
        num = num%10
        res = fmt.Sprintf("%s %s", res, tenList[digit-2])
      }
      if num >= 10 {
        res = fmt.Sprintf("%s %s", res, twoDigitList[num-10])
        num = 0
      }
      res = fmt.Sprintf("%s %s", res, digitList[num])
      return strings.TrimSpace(res)
    }
    
    func numberToWords(num int) string {
      if num == 0 { return "Zero" }
      res := ""
      for _, separator := range []string{"", "Thousand", "Million", "Billion"} {
        if num == 0 { break }
        section := num % 1000
        num = int(num/1000)
        if section != 0 {
          res = fmt.Sprintf("%s %s %s", sectionToWords(section), separator, res)
        }
      }
      return strings.TrimSpace(res)
    }