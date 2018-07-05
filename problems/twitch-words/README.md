
# LintCode: Twitch Words     :BLOG:Basic:

---

Twitch Words  

---

Similar Problems:  

-   Tag: [#slidingwindow](https://code.dennyzhang.com/tag/slidingwindow)

---

Our normal words do not have more than two consecutive letters. If there are three or more consecutive letters, this is a tics. Now give a word, from left to right, to find out the starting point and ending point of all tics.  

Notice  

-   The input string length is n, n <= 100000.

Example  

    Given str = "whaaaaatttsup", return [[2,6],[7,9]].
    
    Explanation:
    "aaaa" and "ttt" are twitching letters, and output their starting and ending points.

    Given str = "whooooisssbesssst", return [[2,5],[7,9],[12,15]].
    
    Explanation:
    "ooo", "sss" and "ssss" are twitching letters, and output their starting and ending points.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/twitch-words)  

Credits To: [lintcode.com](https://www.lintcode.com/en/old/problem/twitch-words/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/twitch-words
    /**
     * @param str: the origin string
     * @return: the start and end of every twitch words
     */
    func twitchWords (str string) [][]int {
        // Basic Ideas: Sliding window
        // Complexity: Time O(n), Space O(1)
        res := [][]int{}
        for i:=0; i<len(str)-2; {
    	if str[i]==str[i+1] && str[i]==str[i+2] {
    	    j:=i+3
    	    for ; j<len(str); j++ {
    		if str[j] != str[i] {break}
    	    }
    	    res = append(res, []int{i, j-1})
    	    i=j
    	} else {
    	    i++
    	}
        }
        return res
    }

