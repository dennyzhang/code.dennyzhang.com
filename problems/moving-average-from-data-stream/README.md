
# Leetcode: Moving Average from Data Stream     :BLOG:Basic:

---

Moving Average from Data Stream  

---

Similar Problems:  

-   Tag: [#oodesign](https://code.dennyzhang.com/tag/oodesign)

---

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.  

For example,  

    MovingAverage m = new MovingAverage(3);
    m.next(1) = 1
    m.next(10) = (1 + 10) / 2
    m.next(3) = (1 + 10 + 3) / 3
    m.next(5) = (10 + 3 + 5) / 3

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/moving-average-from-data-stream)  

Credits To: [leetcode.com](https://leetcode.com/problems/moving-average-from-data-stream/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/moving-average-from-data-stream
    ## Basic Ideas: queue
    ##  Assume the sum will always be an valid integer
    ##
    ## Complexity: Time O(1), Space O(1)
    
    from collections import deque
    class MovingAverage:
        def __init__(self, size):
    	"""
    	Initialize your data structure here.
    	:type size: int
    	"""
    	self.size = size
    	self.q = deque([])
    	self.sum = 0
    
        def next(self, val):
    	"""
    	:type val: int
    	:rtype: float
    	"""
    	if len(self.q) == self.size:
    	    self.sum -= self.q.popleft()
    
    	# add to tail
    	self.q.append(val)
    	self.sum += val
    	return self.sum/len(self.q)
    
    # Your MovingAverage object will be instantiated and called as such:
    # obj = MovingAverage(size)
    # param_1 = obj.next(val)

