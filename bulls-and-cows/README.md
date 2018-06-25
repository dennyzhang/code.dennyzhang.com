
# Leetcode: Bulls and Cows     :BLOG:Basic:

---

Bulls and Cows  

---

Similar Problems:  

-   Tag: [#game](https://code.dennyzhang.com/tag/game), [#string](https://code.dennyzhang.com/tag/string), [#inspiring](https://code.dennyzhang.com/tag/inspiring)

---

You are playing the following [Bulls and Cows game](https://en.wikipedia.org/wiki/Bulls_and_Cows) with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.  

For example:  

    Secret number:  "1807"
    Friend's guess: "7810"

Hint: 1 bull and 3 cows. (The bull is 8, the cows are 0, 1 and 7.)  
Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. In the above example, your function should return "1A3B".  

Please note that both secret number and friend's guess may contain duplicate digits, for example:  

    Secret number:  "1123"
    Friend's guess: "0111"

In this case, the 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow, and your function should return "1A1B".  
You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/bulls-and-cows)  

Credits To: [leetcode.com](https://leetcode.com/problems/bulls-and-cows/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution: 2 arrays with 10 elements; 2 pass

    // Blog link: https://code.dennyzhang.com/bulls-and-cows
    // Basic Ideas: 2 arrays with 10 elements; 2 pass
    // Complexity: Time O(n), Space O(1)
    func getHint(secret string, guess string) string {
        secret_list := [10]int{}
        guess_list := [10]int{}
        bulls, cows := 0, 0
        for i, _ := range secret {
    	if secret[i] == guess[i] {
    	    bulls += 1
    	} else {
    	    secret_list[int(secret[i]-'0')] += 1
    	    guess_list[int(guess[i]-'0')] += 1
    	}
        }
        for i:= 0; i<10; i++ {
    	if secret_list[i] < guess_list[i] {
    	    cows += secret_list[i]
    	} else {
    	    cows += guess_list[i]
    	}
        }
        return fmt.Sprintf("%dA%dB", bulls, cows)
    }

-   Solution: 1 arrays with 10 elements; 1 pass

    // Blog link: https://code.dennyzhang.com/bulls-and-cows
    // Basic Ideas: 1 arrays with 10 elements; 1 pass
    //
    //  array[10]: positive: happen only in secret
    //             negative: happen only in guess
    //
    //  For one specific position, we found ch1 in secret and ch2 in guess
    //    If ch1==ch2, we increase bulls
    //    Otherwise: 
    //       If array[ch1]<0, it means ch1 has happened in guess before. We increase cows
    //       If array[ch2]>0, it means ch2 has happened in secret before. We increase cows
    //       We increase array[ch1] by 1, decrease array[ch2] by 1
    //
    // Complexity: Time O(n), Space O(1)
    func getHint(secret string, guess string) string {
        array := [10]int{}
        bulls, cows := 0, 0
        for i, _ := range secret {
    	ch1, ch2 := secret[i]-'0', guess[i]-'0'
    	if ch1 == ch2 {
    	    bulls += 1
    	    continue
    	}
    	if array[ch1]<0 { cows+=1 }
    	if array[ch2]>0 { cows+=1 }
    	array[ch1] +=1
    	array[ch2] -=1
        }
        return fmt.Sprintf("%dA%dB", bulls, cows)
    }

