# Leetcode: Word Ladder     :BLOG:Basic:


---

Word Ladder  

---

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:  

1.  Only one letter can be changed at a time.
2.  Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

    For example,
    
    Given:
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
    return its length 5.

Note:  
-   Return 0 if there is no such transformation sequence.
-   All words have the same length.
-   All words contain only lowercase alphabetic characters.
-   You may assume no duplicates in the word list.
-   You may assume beginWord and endWord are non-empty and are not the same.

UPDATE (2017/1/20):  
The wordList parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/word-ladder)  

Credits To: [leetcode.com](https://leetcode.com/problems/word-ladder/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/word-ladder
    ## Basic Ideas: BFS. Find the shortest path from point1 to point2
    ##
    ##      How fast we can find the next neighbors?
    ##      Let's say n = len(wordList), w=len(word)
    ##      If check one by one, it would be O(n*w)
    ##
    ##      We can build a set from wordList, then it change 1 characters to all possible combinations
    ##      The complexity would be O(26*w) = O(w)
    ##
    ## Complexity: Time O(?) Space O(n*w)
    ##          n = len(wordList), w=len(word)
    class Solution(object):
        def ladderLength(self, beginWord, endWord, wordList):
            """
            :type beginWord: str
            :type endWord: str
            :type wordList: List[str]
            :rtype: int
            """
            queue, wordSet = [], set(wordList)
            for w in self.findNeighbors(beginWord, wordSet):
                queue.append(w)
    
            level = 1
            while len(queue) != 0:
                level += 1
                for i in xrange(len(queue)):
                    word = queue[0]
                    if word == endWord: return level
                    del queue[0]
                    # find the next candidates
                    for w in self.findNeighbors(word, wordSet):
                        queue.append(w)
            return 0
    
        def findNeighbors(self, word, wordSet):
            l = []
            for i in xrange(len(word)):
                for ascii in range(ord('a'), ord('z')+1):
                    ch = chr(ascii)
                    # skip itself
                    if ch == word[i]: continue
                    newWord = word[:i] + ch+ word[i+1:]
                    # Only if it's unchecked and valid
                    if newWord in wordSet:
                        l.append(newWord)
                        wordSet.remove(newWord)
            return l