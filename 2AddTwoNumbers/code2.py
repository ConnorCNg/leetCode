#https://leetcode.com/problems/add-two-numbers/

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
solution = ListNode()
cur = solution
prev = None
def addTwoNumbers(l1, l2, carry):
    # acount for different length linked lists
    if l1:
        v1 = l1.val
    else:
        v1 = 0
    if l2:
        v2 = l2.val
    else:
        v2 = 0
    
    sum = v1 + v2
    if sum >= 10: # no tens place to carry over
        # integer division (//) moves the tens digit to the ones digit (eg. 351 // 10 = 35). Then use %10 to get the digit in the ones place (eg. 35 % 10 = 5)
        # shouldn't matter in this kind of problem where we're only adding single digit numbers and you'd only ever carry a "1", but future proofing for more than 1 digit per node
        carry = (sum // 10) % 10

    # TODO Determine if last 2 digits are 10 or greater, if so need to append 2 linked list nodes at end instead of 1
    # TODO Exit condition if reached the end of both linked lists so return own node so previous node can point to it
    # TODO If reached reached end of l1 but not l2, recursive call with l1 as None
    # TODO If reached the end of l2 but not l1, recursive call with l2 as None
    # TODO Recursive call

    