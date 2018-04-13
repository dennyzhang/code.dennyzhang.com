# Leetcode: LRU Cache     :BLOG:Hard:


---

LRU Cache  

---

Similar Problems:  
-   [All O\`one Data Structure](https://code.dennyzhang.com/all-oone-data-structure)
-   [Review: Object-Oriented Design Problems](https://code.dennyzhang.com/review-oodesign), Tag: [oodesign](https://code.dennyzhang.com/tag/oodesign)

---

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.  

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.  
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.  

Follow up:  
Could you do both operations in O(1) time complexity?  

Example:  

    LRUCache cache = new LRUCache( 2 /* capacity */ );
    
    cache.put(1, 1);
    cache.put(2, 2);
    cache.get(1);       // returns 1
    cache.put(3, 3);    // evicts key 2
    cache.get(2);       // returns -1 (not found)
    cache.put(4, 4);    // evicts key 1
    cache.get(1);       // returns -1 (not found)
    cache.get(3);       // returns 3
    cache.get(4);       // returns 4

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/lru-cache)  

Credits To: [leetcode.com](https://leetcode.com/problems/lru-cache/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/lru-cache
    ## Basic Ideas: Double linked list + hashmap
    ##
    ##   We need to mapping from dlink to hashmap,
    ##             and also from hashmap to dlink
    ##
    ## Complexity:
    class DLinkNode:
        def __init__(self, val):
            self.val = val
            self.left, self.right = None, None
    
    class LRUCache:
    
        def __init__(self, capacity):
            """
            :type capacity: int
            """
            self.count, self.capacity = 0, capacity
            self.d = {}
            # double link. head is the delete candidates
            self.head, self.tail = DLinkNode(None), DLinkNode(None)
            self.head.right = self.tail
            self.tail.left = self.head
    
        def get(self, key):
            """
            :type key: int
            :rtype: int
            """
            if key in self.d:
                p = self.d[key]
                # remove the node
                p.left.right = p.right
                p.right.left = p.left
                # add to the tail
                p.left = self.tail.left
                p.left.right = p
                p.right = self.tail
                p.right.left = p
                return p.val[1]
            else:
                return -1
    
        def put(self, key, value):
            """
            :type key: int
            :type value: int
            :rtype: void
            """
            if key in self.d:
                self.get(key)
                self.tail.left.val = (key, value)
                return
    
            # need to add one more node
            if self.count == self.capacity:
                # remove one from the head
                p = self.head.right
                p.left.right = p.right
                p.right.left = p.left
                # update related info
                self.count -= 1
                del self.d[p.val[0]]
    
            # create a new node
            p = DLinkNode((key, value))
            # add to tail
            p.left = self.tail.left
            p.left.right = p
            p.right = self.tail
            p.right.left = p
            # update related info
            self.count += 1
            self.d[key] = p
    
    # Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)