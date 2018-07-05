# Leetcode: Similar RGB Color     :BLOG:Basic:


---

Similar RGB Color  

---

Similar Problems:  
-   [Number of Lines To Write String](https://code.dennyzhang.com/number-of-lines-to-write-string)
-   Tag: [#basic](https://code.dennyzhang.com/category/basic), [#string](https://code.dennyzhang.com/category/string)

---

In the following, every capital letter represents some hexadecimal digit from 0 to f.  

The red-green-blue color "#AABBCC" can be written as "#ABC" in shorthand.  For example, "#15c" is shorthand for the color "#1155cc".  

Now, say the similarity between two colors "#ABCDEF" and "#UVWXYZ" is -(AB - UV)^2 - (CD - WX)^2 - (EF - YZ)^2.  

Given the color "#ABCDEF", return a 7 character color that is most similar to #ABCDEF, and has a shorthand (that is, it can be represented as some "#XYZ"  

Example 1:  

    Input: color = "#09f166"
    Output: "#11ee66"
    Explanation:  
    The similarity is -(0x09 - 0x11)^2 -(0xf1 - 0xee)^2 - (0x66 - 0x66)^2 = -64 -9 -0 = -73.
    This is the highest among any shorthand color.

Note:  

-   color is a string of length 7.
-   color is a valid RGB color: for i > 0, color[i] is a hexadecimal digit from 0 to f
-   Any answer which has the same (highest) similarity as the best answer will be accepted.
-   All inputs and outputs should use lowercase letters, and the output is 7 characters.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/similar-rgb-color)  

Credits To: [leetcode.com](https://leetcode.com/problems/similar-rgb-color/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/similar-rgb-color
    ## Basic Ideas:
    ## Complexity: Time O(1): 16*16*16
    ##             Space O(1)
    class Solution:
        def similarRGB(self, color):
            """
            :type color: str
            :rtype: str
            """
            import sys
            l = list("0123456789abcdef")
            colors = [color[1:3], color[3:5], color[5:7]]
            colors_v = []
            for i in range(3):
                colors_v.append(self.hex2DigitsToDecimal(colors[i]))
            min_v, res = sys.maxsize, None
    
            for ch1 in l:
                for ch2 in l:
                    for ch3 in l:
                        colors2 = [ch1+ch1, ch2+ch2, ch3+ch3]
                        diff = 0
                        for i in range(3):
                            v = colors_v[i] - self.hex2DigitsToDecimal(colors2[i])
                            diff += v*v
                            if diff >= min_v: break
                        if diff < min_v:
                            min_v, res = diff, "#"+ ch1+ch1+ch2+ch2+ch3+ch3
            return res
    
        def hex2DigitsToDecimal(self, str):
            res = 0
            [ch1, ch2] = list(str)
            if ch1.isdigit():
                res += ord(ch1)-ord('0')
            else:
                res += ord(ch1)-ord('a') + 10
    
            res = res*16
            if ch2.isdigit():
                res += ord(ch2)-ord('0')
            else:
                res += ord(ch2)-ord('a') + 10
            return res