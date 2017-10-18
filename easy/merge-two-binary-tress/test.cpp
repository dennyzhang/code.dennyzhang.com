//-------------------------------------------------------------------
// @copyright 2017 DennyZhang.com
// Licensed under MIT
// https://www.dennyzhang.com/wp-content/mit_license.txt
//
// File: hello
// Author : Denny <contact@dennyzhang.com>
// Description :
// --
// Created : <2017-10-18>
// Updated: Time-stamp: <2017-10-18 13:34:16>
//-------------------------------------------------------------------
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 * int val;
 * TreeNode *left;
 * TreeNode *right;
 * TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
  TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
    TreeNode* t = new TreeNode(0);
    if ((t1 != NULL) && (t2 != NULL)) {
        t->val = t1->val + t2->val;
        t->left = mergeTrees(t1->left, t2->left);
        t->right = mergeTrees(t1->right, t2->right);
      }
    else {
      if (t1 != NULL) {
          t->val = t1->val;
          t->left = t1->left;
          t->right = t1->right;
        }
      else {
        if (t2 != NULL) {
            t->val = t2->val;
            t->left = t2->left;
            t->right = t2->right;
          }
        else {
          t = NULL;
        }
      }
    }
    return t;
  }
};
// File: hello ends