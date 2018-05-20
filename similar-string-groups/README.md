# Leetcode: Similar String Groups     :BLOG:Medium:


---

Similar String Groups  

---

Similar Problems:  
-   Tag: [#classic](https://code.dennyzhang.com/tag/classic), [#bfs](https://code.dennyzhang.com/tag/bfs)

---

Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y.  

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".  

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.  

We are given a list A of unique strings.  Every string in A is an anagram of every other string in A.  How many groups are there?  

Example 1:  

    Input: ["tars","rats","arts","star"]
    Output: 2

Note:  

1.  A.length <= 2000
2.  A[i].length <= 1000
3.  A.length \* A[i].length <= 20000
4.  All words in A consist of lowercase letters only.
5.  All words in A have the same length and are anagrams of each other.
6.  The judging time limit has been increased for this question.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/similar-string-groups)  

Credits To: [leetcode.com](https://leetcode.com/problems/similar-string-groups/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/similar-string-groups
    // Basic Ideas: BFS + hashmap
    //
    // Choose the firt one to explore
    //
    // Complexity: Time ?, Space ?
    func isSimilar(str1 string, str2 string) bool {
        if len(str1) != len(str2) { return false }
        l := []int{}
        for i:=0; i<len(str1); i++ {
            if str1[i] != str2[i] { l = append(l, i)}
        }
        if len(l) != 2 { return false }
        if str1[l[0]]==str2[l[1]] && str1[l[1]] == str2[l[0]] { return true }
        return false
    }
    
    func numSimilarGroups(A []string) int {
        if len(A) == 0 { return 0 }
    
        res := 0
        unvisited := make(map[int]bool, len(A))
        m := make(map[int]bool, len(A))
        for i:= 0; i<len(A); i++ { unvisited[i] = true }
    
        for i:= 0; i<len(A); i++ {
            if m[i] == true { continue }
            delete(unvisited, i)
            res++
            queue := []int{}
            queue = append(queue, i)
            // explore this word
            for len(queue) != 0 {
                items := []int{}
                for _, i1 := range queue {
                    for i2 := range unvisited {
                        if isSimilar(A[i1], A[i2]) == true {
                            items = append(items, i2)
                            m[i2] = true
                            delete(unvisited, i2)
                        }
                    }
                }
                queue = []int{}
                for _, v:= range items { queue = append(queue, v) }
            }
        }
        return res
    }