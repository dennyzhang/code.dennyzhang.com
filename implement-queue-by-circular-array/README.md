# LintCode: Implement Queue by Circular Array     :BLOG:Basic:


---

Implement Queue by Circular Array  

---

Similar Problems:  
-   [Max Stack](https://code.dennyzhang.com/max-stack)
-   [Review: Object-Oriented Design Problems](https://code.dennyzhang.com/review-oodesign)
-   Tag: [oodesign](https://code.dennyzhang.com/tag/oodesign)

---

Implement queue by circulant array. You need to support the following methods:  
1.  CircularQueue(n): initialize a circular array with size n to store elements
2.  boolean isFull(): return true if the array is full
3.  boolean isEmpty(): return true if there is no element in the array
4.  void enqueue(element): add an element to the queue
5.  int dequeue(): pop an element from the queue  
    
    Notice

it's guaranteed in the test cases we won't call enqueue if it's full and we also won't call dequeue if it's empty. So it's ok to raise exception in scenarios described above.  

Example  

    CircularQueue(5)
    isFull()   => false
    isEmpty() => true
    enqueue(1)
    dequeue()  => 1

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/implement-queue-by-circular-array)  

Credits To: [lintcode](http://www.lintcode.com/en/problem/implement-queue-by-circular-array/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/implement-queue-by-circular-array
    ## Basic Ideas:
    ##  We use (n+1) cells instead of n cells.
    ##  Thus we can differentiate empty case and full case
    ##  self.tail always point to next available cell
    class CircularQueue:
        def __init__(self, n):
            # do intialization if necessary
            self.array = [None]*(n+1)
            self.head, self.tail, self.n = 0, 0, n+1
        """
        @return:  return true if the array is full
        """
        def isFull(self):
            return (self.tail + 1) % self.n == self.head
    
        """
        @return: return true if there is no element in the array
        """
        def isEmpty(self):
            return self.tail == self.head
    
        """
        @param element: the element given to be added
        @return: nothing
        """
        def enqueue(self, element):
            self.array[self.tail] = element
            self.tail = (self.tail+1) % self.n
    
        """
        @return: pop an element from the queue
        """
        def dequeue(self):
            res = self.array[self.head]
            self.head = (self.head+1) % self.n
            return res