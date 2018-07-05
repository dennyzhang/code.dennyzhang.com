
# LintCode: Word Frequency Count     :BLOG:Medium:

---

Word Frequency Count  

---

Similar Problems:  

-   Tag: [#hashmap](https://code.dennyzhang.com/tag/hashmap)

---

Description  
Input a string s and a string list excludeList to find all the most frequent words in s that do not exist in excludeList. Your results will be sorted by lexicographic order by online judge.  

The words are case-insensitive and finally return lowercase words  
Non-alphabetic characters in the string are considered as spaces, and spaces are word separators  
The length of all words does not exceed 10^5​​  and the length a word does not exceed 100  

Example  

    Given s="I love Amazon.", excludeList=[] , return ["i","love","amazon"].
    
    Explanation:
    "i", "love", and "amazon" are the words that appear the most.

    Given s="Do not trouble trouble.", excludeList=["do"], return ["trouble"].
    
    Explanation:
    "trouble" is the most frequently occurring word.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/word-frequency-count)  

Credits To: [lintcode.com](https://www.lintcode.com/problem/word-frequency-count/description)  

Leave me comments, if you have better ways to solve.  

---

-   Solution: dfs

    // Blog link: https://code.dennyzhang.com/word-frequency-count
    // Basic Ideas: hashmap
    // Complexity: Time O(n*log(n)), Space O(n)
    /**
     * @param s: The string s
     * @param excludeList: The excludeList
     * @return: Return the most frequent words
     */
    import ("strings"
    	"sort")
    func getWords (s string, excludeList []string) []string {
        excludeMap := map[string]bool{}
        for _, str := range excludeList { excludeMap[str] = true }
        wordMap := map[string]int{}
        max_count := 0
        s = strings.ToLower(s) + " "
        str := ""
        for _, ch := range s {
    	if ch >= 'a' && ch <= 'z' {
    	    str += string(ch)
    	} else {
    	    if str != "" {
    		if excludeMap[str] == false {
    		    wordMap[str] += 1
    		    if wordMap[str] > max_count { max_count = wordMap[str] }
    		}
    		str = ""
    	    }
    	}
        }
        res := []string{}
        for str := range wordMap {
    	if wordMap[str] == max_count {
    	    res = append(res, str)
    	}
        }
        sort.Strings(res)
        return res
    }

