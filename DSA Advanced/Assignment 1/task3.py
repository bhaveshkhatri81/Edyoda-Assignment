# Merge a linked list into another linked list at alternate positions.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_alternate(head1, head2):
    while head1 is not None and head2 is not None:
        temp1 = head1.next
        temp2 = head2.next

        head1.next = head2
        head2.next = temp1

        head1 = temp1
        head2 = temp2

def print_list(head):
    current = head
    while current is not None:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example Usage
# Construct linked list 1: 1 -> 3 -> 5
list1 = ListNode(1)
list1.next = ListNode(3)
list1.next.next = ListNode(5)

# Construct linked list 2: 2 -> 4 -> 6
list2 = ListNode(2)
list2.next = ListNode(4)
list2.next.next = ListNode(6)

# Merge lists
merge_alternate(list1, list2)

# Print merged list
print_list(list1)
