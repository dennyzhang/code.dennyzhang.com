
# Leetcode: Prefix and Suffix Search     :BLOG:Medium:

---

Prefix and Suffix Search  

---

Similar Problems:  

-   Tag: [#trie](https://code.dennyzhang.com/tag/trie), [#inspiring](https://code.dennyzhang.com/tag/inspiring)

---

Given many words, words[i] has weight i.  

Design a class WordFilter that supports one function, WordFilter.f(String prefix, String suffix). It will return the word with given prefix and suffix with maximum weight. If no word exists, return -1.  

Examples:  

    Input:
    WordFilter(["apple"])
    WordFilter.f("a", "e") // returns 0
    WordFilter.f("b", "") // returns -1

Note:  

1.  words has length in range [1, 15000].
2.  For each test case, up to words.length queries WordFilter.f may be made.
3.  words[i] has length in range [1, 10].
4.  prefix, suffix have lengths in range [0, 10].
5.  words[i] and prefix, suffix queries consist of lowercase letters only.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/prefix-and-suffix-search)  

Credits To: [leetcode.com](https://leetcode.com/problems/prefix-and-suffix-search/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution:

    // Blog link: https://code.dennyzhang.com/prefix-and-suffix-search
    // Basic Ideas: Trie tree
    //
    // Complexity: Time ? Space ?
    type WordFilter struct {
    
    }
    
    
    func Constructor(words []string) WordFilter {
    
    }
    
    
    func (this *WordFilter) F(prefix string, suffix string) int {
    
    }
    
    
    /**
     * Your WordFilter object will be instantiated and called as such:
     * obj := Constructor(words);
     * param_1 := obj.F(prefix,suffix);
     */

