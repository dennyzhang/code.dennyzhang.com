# Leetcode: Count Primes     :BLOG:Medium:


---

Count Primes  

---

Count the number of prime numbers less than a non-negative number, n.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/count-primes)  

Credits To: [leetcode.com](https://leetcode.com/problems/count-primes/description/)  

Leave me comments, if you know how to solve.  

    ## Blog link: http://brain.dennyzhang.com/count-primes
    ## Basic Ideas: Sieve of Eratosthenes
    ##              If n is not a prime, it will have more than 1 dividends.
    ##              One of the dividend must less than sqrt(n)
    ##              1. Find primes from 2 to sqrt(n)
    ##              2. Mark the elements as not prime
    ##              3. The elements which are not visited are prime
    ##
    ## Complexity:
    class Solution(object):
        def countPrimes(self, n):
            """
            :type n: int
            :rtype: int
            """
            if n <= 2:
                return 0
            l = [1] * n
            # l[i] indicate i
            i = 2
            while i*i < n:
                j = 2
                # mark non-prime
                while j*i<n:
                    l[j*i] = 0
                    j += 1
                # move to next prime
                i += 1
                while l[i] == 0 and i*i<n:
                    i += 1
            return sum(l[2::])