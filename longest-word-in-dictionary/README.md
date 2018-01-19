# Leetcode: Longest Word in Dictionary     :BLOG:Basic:


---

Longest Word in Dictionary  

---

Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.  

If there is no answer, return the empty string.  

    Example 1:
    Input: 
    words = ["w","wo","wor","worl", "world"]
    Output: "world"
    Explanation: 
    The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

    Example 2:
    Input: 
    words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    Output: "apple"
    Explanation: 
    Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".

Note:  

-   All the strings in the input will only contain lowercase letters.
-   The length of words will be in the range [1, 1000].
-   The length of words[i] will be in the range [1, 30].

Blog link: <http://brain.dennyzhang.com/longest-word-in-dictionary>  

Github: challenges-leetcode-interesting  

Credits To: leetcode.com  

Leave me comments, if you know how to solve.  

    ## Basic Ideas: trie tree
    ## Complexity: Time O(n), Space O(n). n the count of characters involved
    class TrieNode(object):
        def __init__(self):
            self.children = collections.defaultdict(TrieNode)
            self.is_word = False
    
    class Solution(object):
        def longestWord(self, words):
            """
            :type words: List[str]
            :rtype: str
            """
            # Build TrieNode
            root = TrieNode()
            # check each word, and insert if missing
            for word in words:
                # always check from the top
                node = root
                for ch in word:
                    node = node.children[ch]
                node.is_word = True
    
            return self.foundLongestWord(root)
    
        def foundLongestWord(self, node):
            """
            :rtype: (length, str)
            """
            # BFS:
            # How to check:
            #    Candidates should be: 
            #             1. is_word as true for all nodes in the path. 
            #             2. Has no children
            # How to move to next:
            #   Only check nodes with is_word as True
            #   When node has no children, we 
            max_length, max_str = 0, ''
            queue = []
            # initialize queue
            # Since we have sorted the keys, we will get smallest lexicographical match
            for ch in sorted(node.children):
                child = node.children[ch]
                if child.is_word:
                    queue.append((child, ch, 1))
    
            while len(queue) != 0:
                (node, str, length) = queue[0]
                del queue[0]
                if length > max_length:
                    max_length, max_str = length, str
                for ch in sorted(node.children):
                    child = node.children[ch]
                    if child.is_word:
                        queue.append((child, '%s%s' % (str, ch), length+1))
            return max_str