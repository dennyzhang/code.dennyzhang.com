
# Leetcode: Data Segmentation     :BLOG:Basic:

---

Data Segmentation  

---

Similar Problems:  

-   Tag: [#classic](https://code.dennyzhang.com/tag/classic)

---

Given a string str, we need to extract the symbols and words of the string in order.  

Notice  

-   The length of str does not exceed 10000.
-   The given str contains only lowercase letters, symbols, and spaces.

Example  

    Given str = "(hi (i am)bye)",return ["(","hi","(","i","am",")","bye",")"].
    
    Explanation:
    Separate symbols and words.

    Given str = "#ok yes",return ["#","ok","yes"]
    
    Explanation:
    Separate symbols and words.

    Given str = "##s",return ["#","#","s"]
    
    Explanation:
    Separate symbols and words.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/data-segmentation)  

Credits To: [lintcode.com](http://lintcode.com/en/problem/data-segmentation/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/data-segmentation
    ## Basic Ideas: seperate string
    ## Complexity: Time O(n), Space O(1)
    class Solution:
        """
        @param str: The input string
        @return: The answer
        """
        def dataSegmentation(self, str):
    	res = []
    	word = ""
    	for i, ch in enumerate(str):
    	    if ch.isalpha():
    		word += ch
    	    else:
    		# add caching
    		if word != "":
    		    res.append(word)
    		    word = ""
    		# add current
    		if ch != " ": res.append(ch)
    
    	    # add the last
    	    if i == len(str)-1:
    		if word != "":
    		    res.append(word)
    	return res

