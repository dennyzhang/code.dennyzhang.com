
# Leetcode: Bold Words in String     :BLOG:Basic:

---

Bold Words in String  

---

Similar Problems:  

-   [Add Bold Tag in String](https://code.dennyzhang.com/add-bold-tag-in-string)
-   [Merge Intervals](https://code.dennyzhang.com/merge-intervals)
-   Tag: [#addtag](https://code.dennyzhang.com/tag/addtag), [#inspiring](https://code.dennyzhang.com/tag/inspiring)

---

Given a set of keywords words and a string S, make all appearances of all keywords in S bold. Any letters between <b> and </b> tags become bold.  

The returned string should use the least number of tags possible, and of course the tags should form a valid combination.  

For example, given that words = ["ab", "bc"] and S = "aabcd", we should return "a<b>abc</b>d". Note that returning "a<b>a<b>b</b>c</b>d" would use more tags, so it is incorrect.  

Note:  

1.  words has length in range [0, 50].
2.  words[i] has length in range [1, 10].
3.  S has length in range [0, 500].
4.  All characters in words[i] and S are lowercase letters.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/bold-words-in-string)  

Credits To: [leetcode.com](https://leetcode.com/problems/bold-words-in-string/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/bold-words-in-string
    // Basic Ideas: Merge interval
    // list: marked[bool], then merge the ranges.
    // Complexity: Time O(n*k), Space O(n)
    //             k the total length of words
    func boldWords(words []string, S string) string {
        marked := make([]bool, len(S)+1)
        for i, _ := range S {
    	end := i
    	for _, word := range words {
    	    if strings.Index(S[i:], word) == 0 {
    		if len(word)+i > end { end = len(word)+i }
    	    }
    	}
    	for j:=i; j<end; j++ { marked[j]=true }
        }
    
        ret, has_started := "", false
        for i, ch := range S+";" {
    	if has_started == false && marked[i] == true {
    	    has_started = true
    	    ret += "<b>"
    	}
    	if has_started == true && marked[i] == false {
    	    has_started = false
    	    ret += "</b>"
    	}
    	if ch != ';' { ret += string(ch) }
        }
        return ret
    }

