# Leetcode: Valid Word Square     :BLOG:Medium:


---

Valid Word Square  

---

Similar Problems:  
-   Tag: [#matrixtraverse](https://code.dennyzhang.com/tag/matrixtraverse)

---

Given a sequence of words, check whether it forms a valid word square.  

A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 <= k < max(numRows, numColumns).  

Note:  
The number of words given is at least 1 and does not exceed 500.  
Word length will be at least 1 and does not exceed 500.  
Each word contains only lowercase English alphabet a-z.  
Example 1:  

    Input:
    [
      "abcd",
      "bnrt",
      "crmy",
      "dtye"
    ]
    
    Output:
    true
    
    Explanation:
    The first row and first column both read "abcd".
    The second row and second column both read "bnrt".
    The third row and third column both read "crmy".
    The fourth row and fourth column both read "dtye".
    
    Therefore, it is a valid word square.

Example 2:  

    Input:
    [
      "abcd",
      "bnrt",
      "crm",
      "dt"
    ]
    
    Output:
    true
    
    Explanation:
    The first row and first column both read "abcd".
    The second row and second column both read "bnrt".
    The third row and third column both read "crm".
    The fourth row and fourth column both read "dt".
    
    Therefore, it is a valid word square.

Example 3:  

    Input:
    [
      "ball",
      "area",
      "read",
      "lady"
    ]
    
    Output:
    false
    
    Explanation:
    The third row reads "read" while the third column reads "lead".
    
    Therefore, it is NOT a valid word square.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/valid-word-square)  

Credits To: [leetcode.com](https://leetcode.com/problems/valid-word-square/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/valid-word-square
    ## Basic Ideas:
    ##     What if we can't find the corresponding element?
    ##
    ## Complexity: Time O(m*n), Space O(1)
    class Solution:
        def validWordSquare(self, words):
            """
            :type words: List[str]
            :rtype: bool
            """
            row_count = len(words)
            if row_count == 0: return True
            max_col = 0
            for word in words: max_col = max(max_col, len(word))
            if max_col != row_count: return False
    
            # examine for each row
            try:
                for row_index in range(0, row_count):
                    for k in range(0, len(words[row_index])):
                        if words[row_index][k] != words[k][row_index]:
                            return False
            except:
                return False
            return True