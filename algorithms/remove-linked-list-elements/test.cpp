//-------------------------------------------------------------------
// @copyright 2017 DennyZhang.com
// Licensed under MIT 
//   https://www.dennyzhang.com/wp-content/mit_license.txt
//
// File: hello
// Author : Denny <contact@dennyzhang.com>
// Description :
//   https://leetcode.com/problems/remove-linked-list-elements/description/
// --
// Created : <2017-10-21>
// Updated: Time-stamp: <2017-10-21 22:37:41>
//-------------------------------------------------------------------
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
      ListNode* ret = head;
      ListNode* p;
      ListNode* q;

      if (head == NULL) {
        return NULL;
      }

      p = head;
      q = head;
      while(q) {
        if (q->val != val) {
          p->val = q->val;
          p = p->next;
        }
        q = q->next;
      }
      if (p != NULL) {
        p->next = NULL;
      }
      return head;
    }
};
// File: hello ends
