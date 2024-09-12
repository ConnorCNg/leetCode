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

tests = {
    'a': {
        'l1': [2, 4, 3],
        'l2': [5, 6 ,4],
        'sol': [7, 0 ,8]
     },
     'b': {
         'l1': [9, 9, 9, 9, 9, 9, 9],
         'l2': [9, 9, 9, 9],
         'sol': [8, 9, 9, 9, 0, 0 , 0, 1]
     }
}

def addTwoNumbers(l1, l2, carry=0):
    if not l1 and not l2 and carry == 0:
        return None

    # acount for different length linked lists
    if l1:
        v1 = l1.val
    else:
        v1 = 0
    if l2:
        v2 = l2.val
    else:
        v2 = 0
    
    curVal = v1 + v2 + carry
    carry = 0
    if curVal >= 10: # no tens place to carry over
        # integer division (//) moves the tens digit to the ones digit (eg. 351 // 10 = 35). Then use %10 to get the digit in the ones place (eg. 35 % 10 = 5)
        # shouldn't matter in this kind of problem where we're only adding single digit numbers and you'd only ever carry a "1", but future proofing for more than 1 digit per node
        carry = (curVal // 10) % 10
        curVal = curVal % 10

    curNode = ListNode(curVal)

    '''
    # Exit criteria if reached the end of both lists
    if not l1 and not l2:
        curNode.next = None
        if carry:
            tail = ListNode(carry) # Based on the class above tail.next is None by default
            curNode.next = tail
        curNode.val = curVal
        return curNode
    '''

    # TODO Exit condition if reached the end of both linked lists so return own node so previous node can point to it
    # TODO If reached reached end of l1 but not l2, recursive call with l1 as None
    if l1:
        nextl1 = l1.next
    else:
        nextl1 = None
    # TODO If reached the end of l2 but not l1, recursive call with l2 as None
    if l2:
        nextl2 = l2.next
    else:
        nextl2 = None

    # TODO Recursive call
    curNode.next = addTwoNumbers(nextl1, nextl2, carry)
    return curNode

def listToLinkedList(list):
    cur = head = ListNode(list[0])
    for i in list[1:]:
        cur.next = ListNode(i)
        cur = cur.next
    return head

def linkedListToList(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# Test all
for i in tests:
    print(linkedListToList(addTwoNumbers(listToLinkedList(tests[i]['l1']), listToLinkedList(tests[i]['l2']),0)))

'''
# Test one
i = 'b'
print(linkedListToList(addTwoNumbers(listToLinkedList(tests[i]['l1']), listToLinkedList(tests[i]['l2']),0)))
'''


'''
#Asked ChatGPT to help me format it for Leetcode submission. It also tweaked the syntax a bit.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2, carry=0):
        if not l1 and not l2 and carry == 0:
            return None

        # Account for different length linked lists
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        
        curVal = v1 + v2 + carry
        carry = curVal // 10  # Carry will be either 0 or 1
        curVal = curVal % 10  # Current value will be in the range [0,9]

        curNode = ListNode(curVal)

        # Recursive call
        nextL1 = l1.next if l1 else None
        nextL2 = l2.next if l2 else None
        curNode.next = self.addTwoNumbers(nextL1, nextL2, carry)
        
        return curNode

    def addTwoNumbersWrapper(self, l1, l2):
        return self.addTwoNumbers(l1, l2)
'''