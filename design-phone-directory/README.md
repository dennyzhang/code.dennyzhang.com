# Leetcode: Design Phone Directory     :BLOG:Medium:


---

Design Phone Directory  

---

Similar Problems:  
-   [Review: Object-Oriented Design Problems](https://code.dennyzhang.com/review-oodesign), Tag: [oodesign](https://code.dennyzhang.com/tag/oodesign)

---

Design a Phone Directory which supports the following operations:  

1.  get: Provide a number which is not assigned to anyone.
2.  check: Check if a number is available or not.
3.  release: Recycle or release a number.

Example:  

    // Init a phone directory containing a total of 3 numbers: 0, 1, and 2.
    PhoneDirectory directory = new PhoneDirectory(3);
    
    // It can return any available phone number. Here we assume it returns 0.
    directory.get();
    
    // Assume it returns 1.
    directory.get();
    
    // The number 2 is available, so return true.
    directory.check(2);
    
    // It returns 2, the only number that is left.
    directory.get();
    
    // The number 2 is no longer available, so return false.
    directory.check(2);
    
    // Release number 2 back to the pool.
    directory.release(2);
    
    // Number 2 is available again, return true.
    directory.check(2);

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/design-phone-directory)  

Credits To: [leetcode.com](https://leetcode.com/problems/design-phone-directory/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/design-phone-directory
    ## Basic Ideas: One collection: free_set
    ##
    ##  Notcie: here we only need one collection(free_set), instead of two (occupied_set and free_set)
    ## Complexity: Time O(1), Space O(n)
    class PhoneDirectory(object):
    
        def __init__(self, maxNumbers):
            """
            Initialize your data structure here
            @param maxNumbers - The maximum numbers that can be stored in the phone directory.
            :type maxNumbers: int
            """
            self.free_set = set(range(0, maxNumbers))
    
        def get(self):
            """
            Provide a number which is not assigned to anyone.
            @return - Return an available number. Return -1 if none is available.
            :rtype: int
            """
            return self.free_set.pop() if len(self.free_set) != 0 else -1
    
        def check(self, number):
            """
            Check if a number is available or not.
            :type number: int
            :rtype: bool
            """
            return number in self.free_set
    
        def release(self, number):
            """
            Recycle or release a number.
            :type number: int
            :rtype: void
            """
            if number not in self.free_set: self.free_set.add(number)
    
    # Your PhoneDirectory object will be instantiated and called as such:
    # obj = PhoneDirectory(maxNumbers)
    # param_1 = obj.get()
    # param_2 = obj.check(number)
    # obj.release(number)