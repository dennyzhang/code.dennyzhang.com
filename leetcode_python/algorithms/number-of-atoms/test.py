#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Tags: #redo
## Description:
##     https://leetcode.com/contest/weekly-contest-58/problems/number-of-atoms/
##    ,-----------
##    | Given a chemical formula (given as a string), return the count of each atom.
##    | 
##    | An atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.
##    | 
##    | 1 or more digits representing the count of that element may follow if the count is greater than 1. If the count is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.
##    | 
##    | Two formulas concatenated together produce another formula. For example, H2O2He3Mg4 is also a formula.
##    | 
##    | A formula placed in parentheses, and a count (optionally added) is also a formula. For example, (H2O2) and (H2O2)3 are formulas.
##    | 
##    | Given a formula, output the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.
##    | 
##    | Example 1:
##    | Input: 
##    | formula = "H2O"
##    | Output: "H2O"
##    | Explanation: 
##    | The count of elements are {'H': 2, 'O': 1}.
##    | Example 2:
##    | Input: 
##    | formula = "Mg(OH)2"
##    | Output: "H2MgO2"
##    | Explanation: 
##    | The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
##    | Example 3:
##    | Input: 
##    | formula = "K4(ON(SO3)2)2"
##    | Output: "K4N2O14S4"
##    | Explanation: 
##    | The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
##    | Note:
##    | 
##    | All atom names consist of lowercase letters, except for the first character which is uppercase.
##    | The length of formula will be in the range [1, 1000].
##    | formula will only consist of letters, digits, and round parentheses, and is a valid formula as defined in the problem.
##    `-----------
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 21:01:16>
##-------------------------------------------------------------------
class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        res_dict = self._countOfAtoms(formula)
        # print res_dict
        keys = list(res_dict.keys())
        keys.sort()
        res = ""
        for element in keys:
            if res_dict[element] == 1:
                res = "%s%s" % (res, element)
            else:
                res = "%s%s%d" % (res, element, res_dict[element])                
        return res

    def _countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: dict
        """
        stack = []
        res_dict = {}
        self.uppercase_list = map(chr, range(ord('A'), ord('Z')+1))
        self.lowercase_list = map(chr, range(ord('a'), ord('z')+1))
        self.number_list = map(chr, range(ord('0'), ord('9')+1))

        i = 0
        length = len(formula)
        while i<length:
            ch = formula[i]
            # print("formula: %s, i: %d, ch: %s" %(formula, i, ch))
            if ch in self.lowercase_list:
                stack.append(ch)
                i += 1
            elif ch in self.uppercase_list:
                if len(stack) != 0:
                    (last_element, stack) = self.get_element_from_stack(stack)
                    if res_dict.has_key(last_element):
                        res_dict[last_element] += 1
                    else:
                        res_dict[last_element] = 1
                stack.append(ch)
                i += 1
            elif ch in self.number_list:
                start_index = i
                while i<length and formula[i] in self.number_list:
                    i += 1
                end_index = i
                # stack pop
                (last_element, stack) = self.get_element_from_stack(stack)
                multiple_time = int(''.join(formula[start_index:end_index]))
                # print("number. last_element: %s, stack: %s, multiple_time: %d" % (last_element, stack, multiple_time))
                if res_dict.has_key(last_element):
                    res_dict[last_element] += multiple_time
                else:
                    res_dict[last_element] = multiple_time
                # print "here: %s" % (formula[start_index:end_index])
                # print res_dict
            elif ch == '(':
                # print("here, i:%d" % (i))
                parentheses_count = 1
                i += 1
                j = i
                while i<length and parentheses_count != 0:
                    if formula[i] == '(':
                        parentheses_count += 1
                    elif formula[i] == ')':
                        parentheses_count -= 1
                    i += 1
                # print("parentheses_count: %d, i: %d, parenthese: %s" % (parentheses_count, i, formula[j:i-1]))
                tmp_dict = self._countOfAtoms(formula[j:i-1])

                multiple_time = 1
                if i<length and formula[i] in self.number_list:
                    start_index = i
                    while i<length and formula[i] in self.number_list:
                        i += 1
                    end_index = i
                    multiple_time = int(''.join(formula[start_index:end_index]))

                # print("tmp_dict:%s , multiple_time: %d"  % (tmp_dict, multiple_time))

                # merge
                for element in tmp_dict:
                    if res_dict.has_key(element):
                        res_dict[element] += tmp_dict[element] * multiple_time
                    else:
                        res_dict[element] = tmp_dict[element] * multiple_time

        if len(stack) != 0:
            (element, stack) = self.get_element_from_stack(stack)
            # print("get last element. stack: %s. element: %s" % (stack, element))
            if res_dict.has_key(element):
                res_dict[element] += 1
            else:
                res_dict[element] = 1

        if len(stack) != 0:
            raise Exception("stack should be empty now. stack: %s" % (stack))
        # print res_dict
        return res_dict

    def get_element_from_stack(self, stack):
        #print("get_element_from_stack: stack: %s" % stack)
        if len(stack) == 0:
            return (None, [])

        if stack[-1] in self.uppercase_list:
            return (''.join(stack[-1]), stack[:-2])

        for i in range(len(stack)-1, -1,-1):
            if stack[i] in self.lowercase_list:
                continue
            else:
                break
        # print("stack: %s, i: %d, element: %s, stack: %s" % (stack, i, ''.join(stack[i:]), stack[:i-1]))
        if i == 0:
            return (''.join(stack[i:]), [])
        else:
            return (''.join(stack[i:]), stack[:i-1])