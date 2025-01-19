def makeDoubly(head):
    '''
    :param head: head of the given linked list
    :return: none, just make it doubly linked by assigning ,
             prev pointer accordingly.
    '''

    temp = head
    temp_next = temp.next

    while(temp_next):
        temp_next.prev = temp
        temp = temp_next
        temp_next = temp_next.next

    return
