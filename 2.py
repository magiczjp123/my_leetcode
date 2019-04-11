#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# https://leetcode-cn.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (32.36%)
# Total Accepted:    85.1K
# Total Submissions: 261.4K
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# 
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 
# 示例：
# 
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#     def __str__(self):
#         ss = " = "
#         tmp = self
#         while(tmp != None):
#             ss += "({})".format(tmp.val)
#             tmp = tmp.next
#         return ss

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # special case
        if l1.val == 0 and l1.next == None:
            return l2
        # special case
        elif l2.val == 0 and l2.next == None:
            return l1
        # none zero case
        else:
            # init return value
            rv = ListNode(0)
            # init another marker copy of rv
            cp = rv
            # init carry number as 0
            carry = 0
            count = 0

            while not(l1 == None and l2 == None):
                print("count is {}".format(count))
                count += 1
                
                if l1 == None and l2 != None:
                    current = l2.val + carry
                    cp.val = (current) % 10
                    carry = int((current) / 10)
                    l2 = l2.next

                    
                elif l2 == None and l1 != None:
                    current = l1.val + carry
                    cp.val = (current) % 10
                    carry = int((current) / 10)
                    l1 = l1.next
                    # print("cp.val is {}".format(cp.val))
                    
                else:
                    current = l1.val + l2.val + carry
                    cp.val = (current) % 10
                    carry = int((current) / 10)
                    
                    l1 = l1.next
                    l2 = l2.next

                if l1 == None and l2 == None:
                    if carry:
                        cp.next = ListNode(carry)
                        break
                    else:
                        break
                else:
                    cp.next = ListNode(0)
                    cp = cp.next
                
            return rv

# L = [0,8,6,5,6,8,3,5,7]
# l1 = ListNode(0)
# tmp = l1
# for n in L[:-1]:
#     tmp.val = n
#     tmp.next = ListNode(0)
#     tmp = tmp.next
# tmp.val = L[-1]

# L = [6,7,8,0,8,5,8,9,7]
# l2 = ListNode(0)
# tmp = l2
# for n in L[:-1]:
#     tmp.val = n
#     tmp.next = ListNode(0)
#     tmp = tmp.next
# tmp.val = L[-1]

# print("l1 is {}".format(l1))
# print("l2 is {}".format(l2))
# print("result is {}".format(Solution().addTwoNumbers(l1, l2)))

