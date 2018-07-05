
# Leetcode: Word Break     :BLOG:Medium:

---

Word Break  

---

Similar Problems:  

-   Tag: [#inspiring](https://code.dennyzhang.com/tag/inspiring), [#dynamicprogramming](https://code.dennyzhang.com/tag/dynamicprogramming), [#game](https://code.dennyzhang.com/tag/game)

---

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.  

For example, given  

    s = "leetcode",
    dict = ["leet", "code"].
    
    Return true because "leetcode" can be segmented as "leet code".

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/word-break)  

Credits To: [leetcode.com](https://leetcode.com/problems/word-break/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/word-break
    // Basic Ideas:
    // Complexity:
    func wordBreak(s string, wordDict []string) bool {
        m := map[string]bool{}
        max_len := 0
        for _, word := range wordDict { 
    	m[word] = true
    	if len(word) > max_len { max_len = len(word) }
        }
        l := []int{0}
        status := false
        for i, _ := range s {
    	status = false
    	l2 := []int{}
    	for _, j := range l {
    	    if i+1-j <= max_len {
    		l2 = append(l2, j)
    		str := s[j:i+1]
    		if status == false && m[str] == true {
    		    status = true
    		    l2 = append(l2, i+1)
    		}
    	    }
    	}
    	l = []int{}
    	for _, j := range l2 { l = append(l, j) }
        }
        return status
    }

