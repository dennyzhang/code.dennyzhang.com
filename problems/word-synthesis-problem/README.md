
# Leetcode: Word Synthesis Problem     :BLOG:Medium:

---

Word Synthesis Problem  

---

Similar Problems:  

-   Tag: [#dfs](https://code.dennyzhang.com/tag/dfs), [#inspiring](https://code.dennyzhang.com/tag/inspiring)

---

Description  
Given a target word targets and a collection of n words words, can you select some words from words and select one letter from each word to compose the target word target ?  

Only lowercase letters a-z will be included in the string  
target is no longer than 20, each word in words is no more than 20, and words is no more than 20.  

Example  

    Given target="ally",words=["buy","discard","lip","yep"],return false
    
    Explanation：
    `buy` can match `y`, `discard` can match `a`, `lip` can match `l`, `yep` cannot correspond to any one letter, so there is still one `l` in `target` that cannot be matched. 

    Given target="ray",words=["buy","discard","lip","rep"],return true
    
    Explanation：
    `buy` can match `y`, `discard` can match `a`, `rep` can match `r`.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/word-synthesis-problem)  

Credits To: [lintcode.com](https://www.lintcode.com/problem/word-synthesis-problem/description)  

Leave me comments, if you have better ways to solve.  

---

-   Solution: dfs

    // Blog link: https://code.dennyzhang.com/word-synthesis-problem
    // Basic Ideas: dfs
    // Complexity: 
    /**
     * @param target: the target string
     * @param words: words array
     * @return: whether the target can be matched or not
     */
    var visited = map[int]bool{}
    var chMap = map[rune][]int{}
    
    func dfs(target string) bool {
        if target == "" { return true }
        ch := rune(target[0])
        for _, index := range chMap[ch] {
    	if visited[index] == false {
    	    visited[index] = true
    	    if dfs(target[1:]) == true { return true }
    	    visited[index] = false
    	}
        }
        return false
    }
    
    func matchFunction (target string, words []string) bool {
        for i, word := range words {
    	for _, ch := range word {
    	    chMap[ch] = append(chMap[ch], i)
    	}
        }
        return dfs(target)
    }

