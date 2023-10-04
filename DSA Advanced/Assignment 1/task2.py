# Reverse a linked list in groups of given size

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_in_groups(head, k):
    if not head or k == 1:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    prev_group_end = dummy
    current = head
    count = 0

   
    while current:
        count += 1
        current = current.next

    while count >= k:
        current_group_start = prev_group_end.next
        current_group_end = current_group_start
        next_group_start = current_group_start.next

        for _ in range(k - 1):
            temp = next_group_start.next
            next_group_start.next = current_group_start
            current_group_start = next_group_start
            next_group_start = temp

        prev_group_end.next = current_group_start
        current_group_end.next = next_group_start

        prev_group_end = current_group_end
        count -= k

    return dummy.next

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Create a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print("Original Linked List:")
print_linked_list(head)

# Reverse the linked list in groups of 3
k = 3
new_head = reverse_in_groups(head, k)

print("Linked List after reversing in groups of", k)
print_linked_list(new_head)
