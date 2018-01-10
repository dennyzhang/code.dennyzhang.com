# Leetcode: Insert Delete GetRandom O(1)     :BLOG:Amusing:


---

Design a data structure that supports reqiured operations in O(1) time.  

---

Design a data structure that supports all following operations in average O(1) time.  

1.  insert(val): Inserts an item val to the set if not already present.
2.  remove(val): Removes an item val from the set if present.
3.  getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.

    Example:
    
    // Init an empty set.
    RandomizedSet randomSet = new RandomizedSet();
    
    // Inserts 1 to the set. Returns true as 1 was inserted successfully.
    randomSet.insert(1);
    
    // Returns false as 2 does not exist in the set.
    randomSet.remove(2);
    
    // Inserts 2 to the set, returns true. Set now contains [1,2].
    randomSet.insert(2);
    
    // getRandom should return either 1 or 2 randomly.
    randomSet.getRandom();
    
    // Removes 1 from the set, returns true. Set now contains [2].
    randomSet.remove(1);
    
    // 2 was already in the set, so return false.
    randomSet.insert(2);
    
    // Since 2 is the only number in the set, getRandom always return 2.
    randomSet.getRandom();

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/insert-delete-getrandom-o1)  

Credits To: [Leetcode.com](https://leetcode.com/problems/insert-delete-getrandom-o1/description/)  

Leave me comments, if you know how to solve.  

Useful link: [here](https://discuss.leetcode.com/topic/17564/boyer-moore-majority-vote-algorithm-and-my-elaboration)  

    ## Basic Ideas:
    ##      an array: host all values
    ##           If an existing value has been removed, replace it with the tail. And remove the tail
    ##           If a new value has been added, append to the tail.
    ##           More actions are required. Please see below
    ##      an integer: the length of the array
    ##      a dictionary: host all values and the corresponding index in above array
    ##           Update the index as the values, whenever we add a new value or remove an existing value
    class RandomizedSet(object):
    
        def __init__(self):
            """
            Initialize your data structure here.
            """
            self.dict = {}
            self.array = 
            self.length = 0
            import random
    
        def insert(self, val):
            """
            Inserts a value to the set. Returns true if the set did not already contain the specified element.
            :type val: int
            :rtype: bool
            """
            if val not in self.dict.keys():
                index = self.length
                self.dict[val] = index
                self.array.append(val)
                self.length += 1
                return True
            return False
    
    
        def remove(self, val):
            """
            Removes a value from the set. Returns true if the set contained the specified element.
            :type val: int
            :rtype: bool
            """
            if val in self.dict.keys():
                index = self.dict[val]
                del self.dict[val]
                if index != self.length - 1:
                    self.array[index] = self.array[self.length-1]
                    self.dict[self.array[index]] = index
                del self.array[self.length-1]
                self.length -= 1
                return True
            return False        
    
        def getRandom(self):
            """
            Get a random element from the set.
            :rtype: int
            """
            # error handling
            if self.length == 0:
                return None
            index = random.randint(1, self.length) - 1
            return self.array[index]
    
    # Your RandomizedSet object will be instantiated and called as such:
    # obj = RandomizedSet()
    # param_1 = obj.insert(val)
    # param_2 = obj.remove(val)
    # param_3 = obj.getRandom()

More Reading:  
-   [Leetcode: Majority Element](http://brain.dennyzhang.com/majority-element/)