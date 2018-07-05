
# LintCode: Word Sorting     :BLOG:Basic:

---

Word Sorting  

---

Similar Problems:  

-   [Review: String Problems](https://code.dennyzhang.com/review-string), Tag: [#string](https://code.dennyzhang.com/tag/string)

---

Give a new alphabet, such as {c,b,a,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z}. Sort the string array according to the new alphabet  

Notice  

-   The length of word does not exceed 100.
-   The number of words does not exceed 10000.
-   You can assume that the given new alphabet is a 26-character string.
-   Only lowercase letters.

Example  
Given Alphabet = {c,b,a,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z}, String array = {cab,cba,abc}, return {cba,cab,abc}.  

    Explanation:
    According to the new dictionary order, output the sorted result {cba, cab, abc}.

Given Alphabet = {z,b,a,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,c}, String array = {bca,czb,za,zba,ade}, return {zba,za,bca,ade,czb}.  

    Explanation:
    According to the new dictionary order, output the sorted result {zba,za,bca,ade,czb}.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/word-sorting)  

Credits To: [LintCode.com](http://www.lintcode.com/en/problem/word-sorting/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/word-sorting
    class Solution:
        """
        @param alphabet: the new alphabet
        @param words: the original string array
        @return: the string array after sorting
        """
        def wordSort(self, alphabet, words):
    	import collections
    	self.d = {}
    	v = 0
    	for ch in alphabet:
    	    self.d[ch] = v
    	    v += 1
    	return sorted(words, cmp=self.myCompare)
    
        def myCompare(self, v1, v2):
    	len1, len2 = len(v1), len(v2)
    	if len1<len2: return -self.myCompare(v2, v1)
    	for i in range(0, len2):
    	    ch1, ch2 = v1[i], v2[i]
    	    if self.d[ch1] < self.d[ch2]: return -1
    	    if self.d[ch1] > self.d[ch2]: return 1
    	if len1==len2: return 0
    	else: return 1

