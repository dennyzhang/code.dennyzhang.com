# Leetcode: Reorganize String     :BLOG:Medium:


---

Reorganize String  

---

Similar Problems:  
-   [Review: String Problems](https://brain.dennyzhang.com/review-string), Tag: [#string](https://brain.dennyzhang.com/tag/string)

---

Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.  

If possible, output any possible result.  If not possible, return the empty string.  

Example 1:  

    Input: S = "aab"
    Output: "aba"

Example 2:  

    Input: S = "aaab"
    Output: ""

Note:  

-   S will consist of lowercase letters and have length in range [1, 500].

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/reorganize-string)  

Credits To: [leetcode.com](https://leetcode.com/problems/reorganize-string/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/reorganize-string
    ## Basic Ideas: build a map of duplicated characters
    ##              If the most duplicated characters is no more than half of the items, it's possible.
    ## Complexity: Time O(n), Space O(1)
    class Solution(object):
        def reorganizeString(self, S):
            """
            :type S: str
            :rtype: str
            """
            import collections
            length = len(S)
            m = collections.defaultdict(lambda: 0)
    
            most_count = 0
            for ch in S:
                m[ch] += 1
                most_count = max(most_count, m[ch])
    
            if most_count > (length+1)/2:
                return ''
    
            l = [None]*length
            # how to sort dictionary values
            keys = sorted(m, key=m.get)
            keys = keys[::-1]
    
            for ch in keys:
                count = m[ch]
                i = 0
                # print("ch: %s, count: %d" % (ch, count))
                while i<length:
                    if l[i] is None:
                        break
                    i += 1
    
                # i points to the first None
                while count != 0 and i <length:
                    if l[i] is None:
                        l[i] = ch
                        i = i+2
                        count -= 1
                    else:
                        i = i+1
    
                # remedy
                if count != 0:
                    first_ch = l[0]
                    for k in range(count):
                        i = 2*k
                        l[2*k] = ch
                    # place first_ch to empty places
                    for i in xrange(length):
                        if l[i] is None:
                            l[i] = first_ch
                # print l
            return ''.join(l)
    
    # s = Solution()
    # print s.reorganizeString("tndsewnllhrtwsvxenkscbivijfqnysamckzoyfnapuotmdexzkkrpmppttficzerdndssuveompqkemtbwbodrhwsfpbmkafpwyedpcowruntvymxtyyejqtajkcjakghtdwmuygecjncxzcxezgecrxonnszmqmecgvqqkdagvaaucewelchsmebikscciegzoiamovdojrmmwgbxeygibxxltemfgpogjkhobmhwquizuwvhfaiavsxhiknysdghcawcrphaykyashchyomklvghkyabxatmrkmrfsppfhgrwywtlxebgzmevefcqquvhvgounldxkdzndwybxhtycmlybhaaqvodntsvfhwcuhvuccwcsxelafyzushjhfyklvghpfvknprfouevsxmcuhiiiewcluehpmzrjzffnrptwbuhnyahrbzqvirvmffbxvrmynfcnupnukayjghpusewdwrbkhvjnveuiionefmnfxao")