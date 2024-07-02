class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    values = []
    current = head

    # Traverse the linked list and store values in an array
    while current:
        values.append(current.val)
        current = current.next
    
    # Check if the values form a palindrome using slice operator
    return values == values[::-1]

# Example usage:
# Create a linked list: 1 -> 2 -> 3 -> 2 -> 1
head = ListNode('M')
head.next = ListNode('A')
head.next.next = ListNode('D')
head.next.next.next = ListNode('T')
head.next.next.next.next = ListNode('M')

print(isPalindrome(head))  # Output: True
