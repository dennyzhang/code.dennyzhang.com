
# Leetcode: Goat Latin     :BLOG:Basic:

---

Goat Latin  

---

Similar Problems:  

-   Tag: [#string](https://code.dennyzhang.com/tag/string)

---

A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.  

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)  

The rules of Goat Latin are as follows:  

-   If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.

    For example, the word 'apple' becomes 'applema'.

-   If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".

    For example, the word "goat" becomes "oatgma".

-   Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.

For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.  
Return the final sentence representing the conversion from S to Goat Latin.  

Example 1:  

    Input: "I speak Goat Latin"
    Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

Example 2:  

    Input: "The quick brown fox jumped over the lazy dog"
    Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"

Notes:  

-   S contains only uppercase, lowercase and spaces. Exactly one space between each word.
-   1 <= S.length <= 100.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/goat-latin)  

Credits To: [leetcode.com](https://leetcode.com/problems/goat-latin/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/goat-latin
    // Basic Ideas: Split string as a list first
    // Complexity: Time O(n), Space O(n)
    import "strings"
    func toGoatLatin(S string) string {
        res := ""
        for i, word := range strings.Split(S, " ") {
    	ch := string(word[0])
    	item := ""
    	if strings.Index("aeiouAEIOU", ch) != -1 {
    	    item = word+"ma"
    	} else {
    	    item = word[1:]+ch+"ma"
    	}
    	item = item + strings.Repeat("a", i+1)
    	res += item + " "
        }
        return res[0:len(res)-1]
    }

