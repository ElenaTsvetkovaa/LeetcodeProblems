
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_liked_list(arr):
    dummy = ListNode()
    current = dummy

    for el in arr:
        current.next = ListNode(el)
        current = current.next

    return dummy.next


def merge_sorted_linked_lists(list1, list2):

        while list1 and list2:
            if list1.val < list2.val:
                list1.next = merge_sorted_linked_lists(list1.next, list2)
                return list1
            else:
                list2.next = merge_sorted_linked_lists(list1, list2.next)
                return list2

        if not list1:
            return list2

        if not list2:
            return list1



list1 = create_liked_list([1,2,4])
list2 = create_liked_list([1,3,4])
print(merge_sorted_linked_lists(list1, list2))
