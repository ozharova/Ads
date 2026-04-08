#Part 1
class LinkedListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

# 1
def add_to_beginning(head, value):
    new_node = LinkedListNode(value)
    new_node.next_node = head
    return new_node


# 2
def add_to_end(head, value):
    new_node = LinkedListNode(value)
    if head == None:
        return new_node
    cur = head
    while cur.next_node is not None:
        cur = cur.next_node
    cur.next_node = new_node
    return head


# 3
def remove_last(head):
    if head == None:
        return None
    if head.next_node is None:
        return None
    cur = head
    while cur.next_node.next_node is not None:
        cur = cur.next_node
    cur.next_node = None
    return head

#4
def print_list(head):
    cur = head
    while cur is not None:
        print(cur.value, end=" -> ")
        cur = cur.next_node
    print("None")

# 5
def search_target(head, target):
    cur = head
    while cur is not None:
        if cur.value == target:
            return True
        cur = cur.next_node
    return False


# 6
def insert(head, value, position):
    new_node = LinkedListNode(value)
    if position == 0:
        new_node.next_node = head
        return new_node
    cur = head
    index = 0
    while cur is not None and index != position - 1:
        cur = cur.next_node
        index = index + 1
    if cur is None:
        return head
    new_node.next_node = cur.next_node
    cur.next_node = new_node
    return head

# 7
def remove_by_value(head, target):
    if head is None:
        return None
    if head.value == target:
        return head.next_node
    cur = head
    while cur.next_node is not None:
        if cur.next_node.value == target:
            cur.next_node = cur.next_node.next_node
            return head
        cur = cur.next_node
    return head


# 8
def connect(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    else:
        cur = head1
        while cur.next_node is not None:
            cur = cur.next_node
        cur.next_node = head2
    return head1


# 9
def reverse(head):
    previous = None
    cur = head
    while cur is not None:
        next_node = cur.next_node
        cur.next_node = previous
        previous = cur
        cur = next_node
    return previous
#10
def sort(head):
    sorted = None
    cur = head
    while cur is not None:
        next_node = cur.next_node
        if sorted is None or cur.value < sorted.value:
            cur.next_node = sorted
            sorted = cur
        else:
            temp = sorted
            while temp.next_node is not None and temp.next_node.value < cur.value:
                temp = temp.next_node
            cur.next_node = temp.next_node
            temp.next_node = cur
        cur = next_node
    return sorted


node1 = LinkedListNode(7)
node2 = LinkedListNode(3)
node3 = LinkedListNode(10)

node1.next_node = node2
node2.next_node = node3

print_list(node1)