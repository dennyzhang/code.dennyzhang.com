# Leetcode: Find And Replace in String     :BLOG:Medium:


---

Find And Replace in String  

---

Similar Problems:  
-   Tag: [#string](https://code.dennyzhang.com/tag/string)

---

To some string S, we will perform some replacement operations that replace groups of letters with new ones (not necessarily the same size).  

Each replacement operation has 3 parameters: a starting index i, a source word x and a target word y.  The rule is that if x starts at position i in the original string S, then we will replace that occurrence of x with y.  If not, we do nothing.  

    For example, if we have S = "abcd" and we have some replacement operation i = 2, x = "cd", y = "ffff", then because "cd" starts at position 2 in the original string S, we will replace it with "ffff".

    Using another example on S = "abcd", if we have both the replacement operation i = 0, x = "ab", y = "eee", as well as another replacement operation i = 2, x = "ec", y = "ffff", this second operation does nothing because in the original string S[2] = 'c', which doesn't match x[0] = 'e'.

All these operations occur simultaneously.  It's guaranteed that there won't be any overlap in replacement: for example, S = "abc", indexes = [0, 1], sources = ["ab","bc"] is not a valid test case.  

Example 1:  

    Input: S = "abcd", indexes = [0,2], sources = ["a","cd"], targets = ["eee","ffff"]
    Output: "eeebffff"
    Explanation: "a" starts at index 0 in S, so it's replaced by "eee".
    "cd" starts at index 2 in S, so it's replaced by "ffff".

Example 2:  

    Input: S = "abcd", indexes = [0,2], sources = ["ab","ec"], targets = ["eee","ffff"]
    Output: "eeecd"
    Explanation: "ab" starts at index 0 in S, so it's replaced by "eee". 
    "ec" doesn't starts at index 2 in the original S, so we do nothing.

Notes:  

-   0 <= indexes.length = sources.length = targets.length <= 100
-   0 < indexes[i] < S.length <= 1000
-   All characters in given inputs are lowercase letters.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/find-and-replace-in-string)  

Credits To: [leetcode.com](https://leetcode.com/problems/find-and-replace-in-string/description/)  

Leave me comments, if you have better ways to solve.  

    // Blog link: https://code.dennyzhang.com/find-and-replace-in-string
    // Basic Ideas: One pass. Use hashmap to avoid sorting
    //
    // Notice: indexes may not be in order
    // Test Case: "vmokgggqzp", [3,5,1], ["kg","ggq","mo"], ["s","so","bfr"]
    //
    // Complexity: Time O(n), Space O(n)
    func findReplaceString(S string, indexes []int, sources []string, targets []string) string {
        res := ""
        m := map[int]int{}
        for i, v := range indexes { m[v] = i }
        i := 0
        for i<len(S) {
            index, status := m[i]
            if status == true {
                // check whether we can replace
                word, word_len := sources[index], len(sources[index])
                if len(S)-i < word_len || S[i:i+word_len] != word {
                    res += string(S[i])
                    i++
                } else {
                    // replace
                    i += word_len
                    res += targets[index]
                }
                index += 1
                continue
            }
            res += string(S[i])
            i++
        }
        return res
    }