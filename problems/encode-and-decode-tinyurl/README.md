
# Leetcode: Encode and Decode TinyURL     :BLOG:Basic:

---

Encode and Decode TinyURL  

---

Similar Problems:  

-   [Review: Object-Oriented Design Problems](https://code.dennyzhang.com/review-oodesign)
-   Tag: [oodesign](https://code.dennyzhang.com/tag/oodesign)

---

TinyURL is a URL shortening service where you enter a URL such as [https://leetcode.com/problems/design-tinyurl](https://leetcode.com/problems/design-tinyurl) and it returns a short URL such as [http://tinyurl.com/4e9iAk](http://tinyurl.com/4e9iAk).  

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/encode-and-decode-tinyurl)  

Credits To: [leetcode.com](https://leetcode.com/problems/encode-and-decode-tinyurl/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/encode-and-decode-tinyurl
    class Codec:
        def __init__(self):
    	self.d = {}
    	self.count = 0
    
        def encode(self, longUrl):
    	"""Encodes a URL to a shortened URL.
    
    	:type longUrl: str
    	:rtype: str
    	"""
    	self.count += 1
    	self.d[self.count] = longUrl
    	return str(self.count)
    
        def decode(self, shortUrl):
    	"""Decodes a shortened URL to its original URL.
    
    	:type shortUrl: str
    	:rtype: str
    	"""
    	return self.d[int(shortUrl)]
    
    # Your Codec object will be instantiated and called as such:
    # codec = Codec()
    # codec.decode(codec.encode(url))

