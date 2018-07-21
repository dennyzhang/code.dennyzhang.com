
# Leetcode: Design Linked List     :BLOG:Medium:

---

Design Linked List  

---

Similar Problems:  

-   [Review: Linked List Problems](https://code.dennyzhang.com/review-linkedlist)
-   Tag: [#linkedlist](https://code.dennyzhang.com/tag/linkedlist), [#oodesign](https://code.dennyzhang.com/tag/oodesign)

---

Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list. A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node. If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.  

Implement these functions in your linked list class:  

-   get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
-   addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
-   addAtTail(val) : Append a node of value val to the last element of the linked list.
-   addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
-   deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.

Example:  

    MyLinkedList linkedList = new MyLinkedList();
    linkedList.addAtHead(1);
    linkedList.addAtTail(3);
    linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
    linkedList.get(1);            // returns 2
    linkedList.deleteAtIndex(1);  // now the linked list is 1->3
    linkedList.get(1);            // returns 3

Note:  

-   All values will be in the range of [1, 1000].
-   The number of operations will be in the range of [1, 1000].
-   Please do not use the built-in LinkedList library.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/design-linked-list)  

Credits To: [leetcode.com](https://leetcode.com/problems/design-linked-list/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution:

    // Blog link: https://code.dennyzhang.com/design-linked-list
    type MyLinkedList struct {
    
    }
    
    
    /** Initialize your data structure here. */
    func Constructor() MyLinkedList {
    
    }
    
    
    /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    func (this *MyLinkedList) Get(index int) int {
    
    }
    
    
    /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
    func (this *MyLinkedList) AddAtHead(val int)  {
    
    }
    
    
    /** Append a node of value val to the last element of the linked list. */
    func (this *MyLinkedList) AddAtTail(val int)  {
    
    }
    
    
    /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
    func (this *MyLinkedList) AddAtIndex(index int, val int)  {
    
    }
    
    
    /** Delete the index-th node in the linked list, if the index is valid. */
    func (this *MyLinkedList) DeleteAtIndex(index int)  {
    
    }
    
    
    /**
     * Your MyLinkedList object will be instantiated and called as such:
     * obj := Constructor();
     * param_1 := obj.Get(index);
     * obj.AddAtHead(val);
     * obj.AddAtTail(val);
     * obj.AddAtIndex(index,val);
     * obj.DeleteAtIndex(index);
     */

