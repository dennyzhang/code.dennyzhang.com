
# Leetcode: Prime Palindrome     :BLOG:Medium:

---

Prime Palindrome  

---

Similar Problems:  

-   [Review: Palindrome Problems](https://code.dennyzhang.com/review-palindrome)
-   Tag: [#palindrome](https://code.dennyzhang.com/tag/palindrome), [#math](https://code.dennyzhang.com/tag/math)

---

Find the smallest prime palindrome greater than or equal to N.  

Recall that a number is prime if it's only divisors are 1 and itself, and it is greater than 1.  

For example, 2,3,5,7,11 and 13 are primes.  

Recall that a number is a palindrome if it reads the same from left to right as it does from right to left.  

For example, 12321 is a palindrome.  

Example 1:  

    Input: 6
    Output: 7

Example 2:  

    Input: 8
    Output: 11

Example 3:  

    Input: 13
    Output: 101

Note:  

-   1 <= N <= 10^8
-   The answer is guaranteed to exist and be less than 2 \* 10^8.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/prime-palindrome)  

Credits To: [leetcode.com](https://leetcode.com/problems/prime-palindrome/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution:

    // Blog link: https://code.dennyzhang.com/prime-palindrome
    // Basic Ideas:
    // If palindrome is with odd length, it can't be a prime.
    // It will be able to be divided by 11.
    // Thus we only need to check for the even palindrome
    //
    // Complexity:
    import "strconv"
    func primePalindrome(N int) int {
        if N<=2 { return 2 }
        if N==3 { return 3 }
        if N<=5 { return 5 }
        if N<=7 { return 7 }
        if N<=11 { return 11 }
    	var num int
        for i:=1; i<100000; i++ {
    	str := strconv.Itoa(i)
    	if int(str[0])%2 == 0 { continue }
    	str2 := make([]byte, len(str)*2-1)
    	for j, _ := range str {
    	    str2[j] = str[j]
    	    if j != len(str)-1 {
    		str2[len(str)*2-2-j] = str[j]
    	    }
    	}
    	v, _ := strconv.ParseInt(string(str2), 10, 64)
    		num = int(v)
    	if num>=N && isPrime(num) { return num }
        }
        return -1
    }
    
    func isPrime(N int) bool {
        if (N<2 || N%2 == 0) { return N == 2}
        for i:=3; i*i<=N; i += 2 {
    	if N%i == 0 { return false }
        }
        return true
    }

