
# Leetcode: Kth Largest Element in a Stream     :BLOG:Medium:

---

Kth Largest Element in a Stream  

---

Similar Problems:  

-   [Leetcode: Kth Largest Element in an Array](https://code.dennyzhang.com/kth-largest-element-in-an-array)
-   [Review: Heap Problems](https://code.dennyzhang.com/review-heap)
-   [Tag: #heap](https://code.dennyzhang.com/tag/heap)

---

Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.  

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.  

Example:  

    int k = 3;
    int[] arr = [4,5,8,2];
    KthLargest kthLargest = new KthLargest(3, arr);
    kthLargest.add(3);   // returns 4
    kthLargest.add(5);   // returns 5
    kthLargest.add(10);  // returns 5
    kthLargest.add(9);   // returns 8
    kthLargest.add(4);   // returns 8

Note:  

-   You may assume that nums' length >= k-1 and k >= 1.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/kth-largest-element-in-a-stream)  

Credits To: [leetcode.com](https://leetcode.com/problems/kth-largest-element-in-a-stream/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution: heap

    ## Blog link: https://code.dennyzhang.com/kth-largest-element-in-a-stream
    ## Basic Ideas: min heap
    ## Complexity: Time O(log(k)), Space O(k)
    import heapq
    class KthLargest:
    
        def __init__(self, k, nums):
    	"""
    	:type k: int
    	:type nums: List[int]
    	"""
    	self.q = []
    	self.k = k
    	for num in nums:
    	    heapq.heappush(self.q, num)
    	    if len(self.q) > k: heapq.heappop(self.q)
    
        def add(self, val):
    	"""
    	:type val: int
    	:rtype: int
    	"""
    	heapq.heappush(self.q, val)
    	if len(self.q) > self.k: heapq.heappop(self.q)
    	return self.q[0]
    
    # Your KthLargest object will be instantiated and called as such:
    # obj = KthLargest(k, nums)
    # param_1 = obj.add(val)

