
# Leetcode: Encode and Decode Strings     :BLOG:Medium:

---

Encode and Decode Strings  

---

Similar Problems:  

-   Tag: [#string](https://code.dennyzhang.com/tag/string), [#classic](https://code.dennyzhang.com/tag/classic), [#oodesign](https://code.dennyzhang.com/tag/oodesign)

---

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.  

Machine 1 (sender) has the function:  

    string encode(vector<string> strs) {
      // ... your code
      return encoded_string;
    }

Machine 2 (receiver) has the function:  

    vector<string> decode(string s) {
      //... your code
      return strs;
    }

So Machine 1 does:  

    string encoded_string = encode(strs);

and Machine 2 does:  

    vector<string> strs2 = decode(encoded_string);

strs2 in Machine 2 should be the same as strs in Machine 1.  

Implement the encode and decode methods.  

Note:  

-   The string may contain any possible characters out of 256 valid ascii characters. Your algorithm should be generalized enough to work on any possible characters.
-   Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
-   Do not rely on any library method such as eval or serialize methods. You should implement your own encode/decode algorithm.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/encode-and-decode-strings)  

Credits To: [leetcode.com](https://leetcode.com/problems/encode-and-decode-strings/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution: Encode with length

    ## Blog link: https://code.dennyzhang.com/encode-and-decode-strings
    ## Basic Ideas:
    ## [count_of_strings] [length1] string1[length2] string2...
    ## Complexity:
    class Codec:
    
        def encode(self, strs):
    	"""Encodes a list of strings to a single string.
    
    	:type strs: List[str]
    	:rtype: str
    	"""
    	res = "%d " % len(strs)
    	for s in strs:
    	    res = "%s%d %s" % (res, len(s), s)
    	return res
    
        def decode(self, s):
    	"""Decodes a single string to a list of strings.
    
    	:type s: str
    	:rtype: List[str]
    	"""
    	if s == "": return []
    	res = []
    	i = 0
    	while s[i] != ' ': i += 1
    	count = int(s[0:i])
    	i += 1
    
    	for k in range(count):
    	    # get length
    	    j = i
    	    while s[j] != ' ': j += 1
    	    length = int(s[i:j])
    	    i = j+1
    	    # get string
    	    res.append(s[i:i+length])
    	    i = i+length
    	return res
    
    # Your Codec object will be instantiated and called as such:
    # codec = Codec()
    # codec.decode(codec.encode(strs))

---

-   Solution: Encode with length

    ## Blog link: https://code.dennyzhang.com/encode-and-decode-strings
    ## Basic Ideas:
    ## [length1] string1[length2] string2...
    ## Complexity:
    class Codec:
    
        def encode(self, strs):
    	"""Encodes a list of strings to a single string.
    
    	:type strs: List[str]
    	:rtype: str
    	"""
    	res = ""
    	for s in strs:
    	    res = "%s%d %s" % (res, len(s), s)
    	return res
    
        def decode(self, s):
    	"""Decodes a single string to a list of strings.
    
    	:type s: str
    	:rtype: List[str]
    	"""
    	if s == "": return []
    	res = []
    	i = 0
    	while i<len(s):
    	    # get length
    	    j = i
    	    while s[j] != ' ': j += 1
    	    length = int(s[i:j])
    	    i = j+1+length
    	    # get string
    	    res.append(s[j+1:i])
    	return res
    
    
    # Your Codec object will be instantiated and called as such:
    # codec = Codec()
    # codec.decode(codec.encode(strs))

---

-   Solution: Use invisible character as separator

    ## Blog link: https://code.dennyzhang.com/encode-and-decode-strings
    ## Basic Ideas:
    ## Use invisible character as separator
    ## Differentiate two cases: empty list, items with empty strings
    ## Complexity:
    class Codec:
    
        def encode(self, strs):
    	"""Encodes a list of strings to a single string.
    	:type strs: List[str]
    	:rtype: str
    	"""
    	if len(strs) == 0: return "\n"
    	return "\t".join(strs)
    
        def decode(self, s):
    	"""Decodes a single string to a list of strings.
    	:type s: str
    	:rtype: List[str]
    	"""
    	if s == "\n": return []
    	return s.split('\t')

