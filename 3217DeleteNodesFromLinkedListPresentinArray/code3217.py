# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/?envType=daily-question&envId=2024-09-06
#3217. Delete Nodes From Linked List Present in Array

#You are given an array of integers nums and the head of a linked list. Return the head of the modified linked list after removing all nodes from the linked list that have a value that exists in nums.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
tests = {
    'a': {
        'head': [1, 2, 3 ,4 ,5],
        'nums': [1, 2 ,3],
        'sol': [4, 5]
     },
     'b': {
         'head': [1, 2, 1, 2, 1, 2],
         'nums': [1],
         'sol': [2, 2, 2]
     }
}
"""

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

def deleteNodes(nums, head):
    nums_dict = {key: None for key in nums}
    cur = head
    prev = None
    while cur is not None:
        #print(cur.val)
        if cur.val in nums_dict:
            if prev: 
                prev.next = cur.next
                cur = cur.next
            else: # Only other case should be that we're at the head of the linked list
                head = cur.next # Set the head of the linked list to the next node
                head.next = cur.next.next # Set the pointer of the new head to the pointer's pointer
                cur = head # Set the current node to the head/next node
        else:
            prev = cur
            cur = cur.next
    return head
"""
# Test all
for i in tests:
    print(deleteNodes(tests[i]['nums'], listToLinkedList(tests[i]['head'])))

# Test one
i = 'b'
print(deleteNodes(tests[i]['nums'], listToLinkedList(tests[i]['head'])))
"""