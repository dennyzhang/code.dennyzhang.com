# Leetcode: Word Search II     :BLOG:Hard:


---

Word Search II  

---

Similar Problems:  
-   Tag: [#backtracking](https://code.dennyzhang.com/tag/backtracking)

---

Given a 2D board and a list of words from the dictionary, find all words in the board.  

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.  

For example,  

    Given words = ["oath","pea","eat","rain"] and board =
    
    [
      ['o','a','a','n'],
      ['e','t','a','e'],
      ['i','h','k','r'],
      ['i','f','l','v']
    ]
    Return ["eat","oath"].

Note:  
You may assume that all inputs are consist of lowercase letters a-z.  

    You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?
    
    If the current candidate does not exist in all words' prefix, you
    could stop backtracking immediately. What kind of data structure could
    answer such query efficiently? Does a hash table work? Why or why not?
    How about a Trie? If you would like to learn how to implement a basic
    trie, please work on this problem: Implement Trie (Prefix Tree) first.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/word-search-ii)  

Credits To: [leetcode.com](https://leetcode.com/problems/word-search-ii/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/word-search-ii