# Leetcode: Add Bold Tag in String     :BLOG:Medium:


---

Add Bold Tag in String  

---

Similar Problems:  
-   [Bold Words in String](https://code.dennyzhang.com/bold-words-in-string)
-   [Jump Game](https://code.dennyzhang.com/jump-game)
-   Tag: [#addtag](https://code.dennyzhang.com/tag/addtag)

---

Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.  
Example 1:  

    Input: 
    s = "abcxyz123"
    dict = ["abc","123"]
    Output:
    "<b>abc</b>xyz<b>123</b>"

Example 2:  

    Input: 
    s = "aaabbcc"
    dict = ["aaa","aab","bc"]
    Output:
    "<b>aaabbc</b>c"

Note:  
1.  The given dict won't contain duplicates, and its length won't exceed 100.
2.  All the strings in input have length in range [1, 1000].

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/add-bold-tag-in-string)  

Credits To: [leetcode.com](https://leetcode.com/problems/add-bold-tag-in-string/description/)  

Leave me comments, if you have better ways to solve.  

    // Blog link: https://code.dennyzhang.com/add-bold-tag-in-string
    // Basic Ideas: Merge ranges
    // Complexity: Time O(n*w), Space O(n)
    //             w = total length of dict
    func addBoldTag(s string, dict []string) string {
        marked := make([]bool, len(s)+1)
        for i, _ := range s {
            end := i
            for _, word := range dict {
                if strings.Index(s[i:], word) == 0 {
                    if len(word)+i>end { end = len(word)+i }
                }
            }
            for j:=i; j<end; j++ { marked[j] = true }
        }
        res, has_started := "", false
        for i, ch := range s+";" {
            if marked[i] == true && has_started == false {
                has_started = true
                res += "<b>"
            }
            if marked[i] == false && has_started == true {
                has_started = false
                res += "</b>"
            }
            if ch != ';' { res += string(ch) }
        }
        return res
    }