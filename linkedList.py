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

    def reverse_list(self, head: ListNode) -> ListNode:
        # final condition
        if head is None or head.next is None:
            return head

        # current work
        tmp = self.reverse_list(head.next)
        head.next.next = head
        head.next = None
        return tmp

    # not completed ##########
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head is None or head.next is None: return head
        tmp = head
        l_part = head
        r_part = None
        count = 1
        while count < m-1:
            tmp = tmp.next
            count += 1
        l_part = tmp
        tmp = tmp.next
        end = tmp
        while count <= n:
            r_part = tmp.next
            tmp.next = l_part
            tmp = r_part

            count += 1

        l_part.next = tmp
        end.next = tmp.next

        return head


L = [1,2,3,4,5]
l = ListNode(0)
tmp = l
for n in L[:-1]:
    tmp.val = n
    tmp.next = ListNode(0)
    tmp = tmp.next
tmp.val = L[-1]

print("l is {}".format(l))
print("result is {}".format(Solution().reverseBetween(l, 2, 4)))
