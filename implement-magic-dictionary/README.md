# Leetcode: Implement Magic Dictionary     :BLOG:Amusing:


---

Implement Magic Dictionary  

---

Similar Problems:  
-   [Review: Object-Oriented Design Problems](https://code.dennyzhang.com/review-oodesign)
-   Tag: [oodesign](https://code.dennyzhang.com/tag/oodesign)

---

Implement a magic directory with buildDict, and search methods.  

For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.  

For the method search, you'll be given a word, and judge whether if you modify exactly one character into another character in this word, the modified word is in the dictionary you just built.  

Example 1:  

    Input: buildDict(["hello", "leetcode"]), Output: Null
    Input: search("hello"), Output: False
    Input: search("hhllo"), Output: True
    Input: search("hell"), Output: False
    Input: search("leetcoded"), Output: False

Note:  
1.  You may assume that all the inputs are consist of lowercase letters a-z.
2.  For contest purpose, the test data is rather small by now. You could think about highly efficient algorithm after the contest.
3.  Please remember to RESET your class variables declared in class MagicDictionary, as static/class variables are persisted across multiple test cases. Please see here for more details.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/implement-magic-dictionary)  

Credits To: [leetcode.com](https://leetcode.com/problems/implement-magic-dictionary/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/implement-magic-dictionary
    ## Basic Ideas: Trie Tree + recursive
    ##
    ## Complexity: Time O(w*h): w is the width, h is the height
    ##             Space O(n): n sum of all characters in dict
    import collections
    class TrieNode:
        def __init__(self):
            self.children = collections.defaultdict(TrieNode)
            self.is_word = False
    
    class Trie:
        def __init__(self):
            self.root = TrieNode()
    
        def addWord(self, trieNode, word):
            node = trieNode
            for ch in word:
                node = node.children[ch]
            node.is_word = True
    
        def searchWord(self, trieNode, word):
            node = trieNode
            for ch in word:
                if ch not in node.children:
                    return False
                node = node.children[ch]
            return node.is_word
    
    class MagicDictionary:
    
        def __init__(self):
            """
            Initialize your data structure here.
            """
            self.myTrie = Trie()
    
    
        def buildDict(self, dict):
            """
            Build a dictionary through a list of words
            :type dict: List[str]
            :rtype: void
            """
            for word in dict:
                self.myTrie.addWord(self.myTrie.root, word)
    
        def search(self, word):
            """
            Returns if there is any word in the trie that equals to the given word after modifying exactly one character
            :type word: str
            :rtype: bool
            """
            if len(word) == 0: return False
            (status, cnt) = self.mySearch(self.myTrie, self.myTrie.root, word, False)
            return (status is True) and (cnt == 1)
    
        def mySearch(self, trie, trieNode, word, exactMatch):
            """
            :rtype: (bool, cnt)
            """
            # base cases for recursive
            if exactMatch == True:
                status = trie.searchWord(trieNode, word)
                return (status, 0)
    
            if len(word) == 1:
                for ch in trieNode.children:
                    if word[0] != ch and trieNode.children[ch].is_word:
                        return (True, 1)
                return (False, 0)
    
            for ch in trieNode.children:
                # difference happens in the next layer
                if word[0] == ch:
                    (status, cnt) = self.mySearch(trie, trieNode.children[ch], word[1:], False)
                    if (status is True) and (cnt == 1): return (True, 1)
                else:
                    # difference happens in the current layer
                    (status, cnt) = self.mySearch(trie, trieNode.children[ch], word[1:], True)
                    if (status is True) and (cnt == 0): return (True, 1)
            return (False, 0)
    
    # Your MagicDictionary object will be instantiated and called as such:
    # obj = MagicDictionary()
    # obj.buildDict(dict)
    # param_2 = obj.search(word)