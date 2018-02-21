# Leetcode: Find Median from Data Stream     :BLOG:Amusing:


---

Find Median from Data Stream  

---

Similar Problems:  
-   [Median of Two Sorted Arrays](https://brain.dennyzhang.com/median-of-two-sorted-arrays)
-   Tag: [#oodesign](https://brain.dennyzhang.com/tag/oodesign)

---

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.  

Examples:  

    [2,3,4] , the median is 3
    
    [2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:  

void addNum(int num) - Add a integer number from the data stream to the data structure.  
double findMedian() - Return the median of all elements so far.  
For example:  

    addNum(1)
    addNum(2)
    findMedian() -> 1.5
    addNum(3) 
    findMedian() -> 2

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/find-median-from-data-stream)  

Credits To: [leetcode.com](https://leetcode.com/problems/find-median-from-data-stream/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/find-median-from-data-stream
    ## Basic Ideas: Use 2 heaps: 
    ##      maxheap for the first half, minheap for the second half
    ##
    ##  Notice: When taking new values, we can't appeneding them directly.
    ##          It will not be an ordred integer list then.
    ##          What if we have duplicate values
    ##
    ## Complexity: Time O(log(n)), Space O(n)
    import heapq
    class MedianFinder:
    
        def __init__(self):
            """
            initialize your data structure here.
            """
            self.left_q, self.right_q = [], []
            heapq.heapify(self.left_q)
            heapq.heapify(self.right_q)
    
        def addNum(self, num):
            """
            :type num: int
            :rtype: void
            """
            if len(self.left_q) == 0:
                heapq.heappush(self.left_q, -num)
                return
    
            if num <= -self.left_q[0]:
                # should insert to left
                heapq.heappush(self.left_q, -num)
                # rebalancing
                if len(self.left_q) > len(self.right_q)+1:
                    element = -heapq.heappop(self.left_q)
                    heapq.heappush(self.right_q, element)
            else:
                heapq.heappush(self.right_q, num)
                # rebalancing
                if len(self.right_q) > len(self.left_q):
                    new_element = -heapq.heappop(self.right_q)
                    heapq.heappush(self.left_q, new_element)
    
        def findMedian(self):
            """
            :rtype: float
            """
            if len(self.left_q) == 0: return None
            if (len(self.left_q) == len(self.right_q)):
                return (-self.left_q[0] + self.right_q[0])/2
            else:
                return float(-self.left_q[0])
    
    # Your MedianFinder object will be instantiated and called as such:
    # obj = MedianFinder()
    # obj.addNum(num)
    # param_2 = obj.findMedian()