import pytest

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
     },
     'c': {
         'l1': [0],
         'l2': [0],
         'sol': [0]
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
    from code2 import addTwoNumbers
    for i in tests:
        assert linkedListToList(addTwoNumbers(listToLinkedList(tests[i]['l1']), listToLinkedList(tests[i]['l2']))) == tests[i]['sol']

if __name__ == "__main__":
    pytest.main()