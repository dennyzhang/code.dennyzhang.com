
# Leetcode: Roman to Integer     :BLOG:Basic:

---

Roman to Integer  

---

Similar Problems:  

-   [Integer to Roman](https://code.dennyzhang.com/integer-to-roman)
-   Tag: [#math](https://code.dennyzhang.com/tag/math)
-   [Review: Linked List Problems](https://code.dennyzhang.com/review-linkedlist), [Tag: #linkedlist](https://code.dennyzhang.com/tag/linkedlist)

---

Given a roman numeral, convert it to an integer.  

Input is guaranteed to be within the range from 1 to 3999.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/roman-to-integer)  

Credits To: [leetcode.com](https://leetcode.com/problems/roman-to-integer/description/)  

Leave me comments, if you have better ways to solve.  

---

<<<<<<< HEAD  
Reference:  

-   [wikipedia: Roman numerals](https://en.wikipedia.org/wiki/Roman_numerals#Roman_numeric_system)
-   [Roman Numerals Chart](http://literacy.kent.edu/Minigrants/Cinci/romanchart.htm)

    // Blog link: https://code.dennyzhang.com/roman-to-integer
    // Related reading: 
    // Basic Ideas: Examine from left to right.
    //   If current is smaller than the next, substract. 
    //   Otherwise, add
    //
    // Complexity: Time O(1), Space O(1)
    func romanToInt(s string) int {
        m := map[byte]int{'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res := 0
        for i, _ := range s {
    	if i == len(s)-1 {
    	    res += m[s[i]]
    	} else{
    	    if m[s[i]] < m[s[i+1]] {
    		res -= m[s[i]]
    	    } else {
    		res += m[s[i]]
    	    }
    	}
        }
        return res
    }
    =======
    #+BEGIN_SRC python
    ## Blog link: https://code.dennyzhang.com/roman-to-integer
    
    >>>>>>> 123cc57c2e4abe14e48c40bfd5bdc5982e4e0c29

