def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head or not head.next or k == 0:
        return head

    # Calculate the length of the linked list
    length = 1
    current = head
    while current.next:
        current = current.next
        length += 1

    # Calculate the actual number of rotations needed
    k = k % length
    if k == 0:
        return head

    # Break the list into two parts
    current.next = head
    steps = length - k
    current = head
    for _ in range(steps - 1):
        current = current.next

    # Update the head
    new_head = current.next
    current.next = None

    return new_head