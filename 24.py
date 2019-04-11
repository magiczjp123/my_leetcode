#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#
# https://leetcode-cn.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (56.84%)
# Total Accepted:    13.4K
# Total Submissions: 23.6K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 
# 
# 
# 示例:
# 
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        ss = " = "
        tmp = self
        while(tmp != None):
            ss += "({})".format(tmp.val)
            tmp = tmp.next
        return ss

class Solution:

    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        tmp = head.next
        head.next = self.swapPairs(tmp.next)
        tmp.next = head

        return tmp


L = [1,2,3,4,5,6,7]
l = ListNode(0)
tmp = l
for n in L[:-1]:
    tmp.val = n
    tmp.next = ListNode(0)
    tmp = tmp.next
tmp.val = L[-1]

print("l is {}".format(l))
print("result is {}".format(Solution().swapPairs(l)))


