import pytest

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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
     },
     'c': {
         'head': [1, 2, 3, 4],
         'nums': [5],
         'sol': [1, 2, 3, 4]
     }
}

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

def test_solutions():
    from code3217 import deleteNodes
    for i in tests:
        assert linkedListToList(deleteNodes(tests[i]['nums'], listToLinkedList(tests[i]['head']))) == tests[i]['sol']

if __name__ == "__main__":
    pytest.main()