# Delete the elements in an linked list whose sum is equal to zero

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_zero_sum_nodes(head):
    cumulative_sum = 0
    sum_dict = {}
    current = head
    
    while current is not None:
        cumulative_sum += current.data
        
        if cumulative_sum == 0:
            head = current.next
            sum_dict = {}  # Reset the dictionary for zero sum
            
        if cumulative_sum in sum_dict:
            sum_dict[cumulative_sum].next = current.next
        else:
            sum_dict[cumulative_sum] = current
        
        current = current.next
    
    return head

def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Create a sample linked list: 6 -> -6 -> 8 -> 4 -> -12 -> 9 -> 8
head = Node(6)
head.next = Node(-6)
head.next.next = Node(8)
head.next.next.next = Node(4)
head.next.next.next.next = Node(-12)
head.next.next.next.next.next = Node(9)
head.next.next.next.next.next.next = Node(8)

print("Original Linked List:")
print_list(head)

head = delete_zero_sum_nodes(head)

print("\nLinked List after deleting nodes with zero sum:")
print_list(head)
