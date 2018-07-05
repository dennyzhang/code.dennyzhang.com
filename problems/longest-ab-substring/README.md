
# LintCode: Longest AB Substring     :BLOG:Medium:

---

Longest AB Substring  

---

Similar Problems:  

-   [Lintcode: Same Number](https://code.dennyzhang.com/same-number)
-   Tag: [#hashmap](https://code.dennyzhang.com/tag/hashmap)

---

Description  
Given a string s of only 'A' and 'B', find the longest substring that satisfies the number of 'A' and 'B' are the same. Please output the length of this substring.  

n is the length of s, 2<=n<=1000000.  

Example  

    Given s = "ABAAABBBA", return 8.
    
    Explanation:
    Substring s[0,7] and s[1,8] meet the conditions, their length is 8.

    Given s = "AAAAAA", return 0.
    
    Explanation:
    No substring satisfies the condition except empty substring.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/longest-ab-substring)  

Credits To: [lintcode.com](https://www.lintcode.com/problem/longest-ab-substring/description)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/longest-ab-substring
    // Basic Ideas:
    // A: +1, B -1
    //   S: A B A A B B A
    //   l: 1 0 1 2 1 0 1
    // For l[i], find the farest index of the possible matches
    // To speed up the lookup, use hashmap
    // Complexity: Time O(n), Space O(n)
    func getAns (S string) int {
        m := map[int]int{}
        l := make([]int, len(S))
        v := 0
        for i, ch := range S {
    	if ch == 'A' {
    	    v++
    	} else {
    	    v--
    	}
    	l[i] = v
    	if i>m[v] { m[v] = i }
        }
        res := 0
        for i := 0; i<len(S)-1; i++ {
    	target := l[i]
    	if S[i] == 'A' {
    	    target--
    	} else {
    	    target++
    	}
    	if m[target] > i {
    	    if m[target]-i+1 > res { res = m[target]-i+1 }
    	}
        }
        return res
    }

