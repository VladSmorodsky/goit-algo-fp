class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"[Node data: {self.data}]"


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = Node(data)

    def insert_at_start(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        node = Node(data)
        node.next = prev_node.next
        prev_node.next = node

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return current_node
            current_node = current_node.next
        return None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node)
            current_node = current_node.next

    def delete(self, deleted_data):
        current_node = self.head
        if current_node and current_node.data == deleted_data:
            self.head = None
            current_node = None
            return
        prev_node = None
        while current_node.data != deleted_data:
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            return
        prev_node.next = current_node.next
        current_node = None


def reverse_linked_list(linked_list: LinkedList) -> None:
    """
    Reverses the given linked list in place.
    """
    if not linked_list.head:
        return
    current_element = linked_list.head
    prev_element = None
    while current_element:
        next_element = current_element.next
        current_element.next = prev_element
        prev_element = current_element
        current_element = next_element
    linked_list.head = prev_element


def sort_linked_list(linked_list: LinkedList) -> None:
    """
    Sorts the linked list using insertion sort algorithm.
    """
    if not linked_list.head or not linked_list.head.next:
        return
    pseudo_head_element = Node(None)
    curr_element = linked_list.head

    while curr_element:
        next_element = curr_element.next
        prev_element = pseudo_head_element
        while prev_element.next and prev_element.next.data < curr_element.data:
            prev_element = prev_element.next
        curr_element.next = prev_element.next
        prev_element.next = curr_element

        curr_element = next_element
    linked_list.head = pseudo_head_element.next


def merge_sorted_lists(linked_list1: LinkedList, linked_list2: LinkedList) -> LinkedList:
    """
    Merges two sorted linked lists into a new sorted linked list.
    """
    merged_list = LinkedList()
    temp_start_node = Node(0)
    tail = temp_start_node

    head1, head2 = linked_list1.head, linked_list2.head

    while head1 and head2:
        if head1.data <= head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next

    if head1:
        tail.next = head1
    elif head2:
        tail.next = head2

    merged_list.head = temp_start_node.next

    return merged_list


llist = LinkedList()

llist.insert_at_start(5)
llist.insert_at_start(10)
llist.insert_at_start(15)

llist.insert_at_end(20)
llist.insert_at_end(25)

print("Reverse list:")
reverse_linked_list(llist)
llist.print_list()

print('Sort list:')
sort_linked_list(llist)
llist.print_list()

print('Merge 2 sorted lists:')

llist2 = LinkedList()
llist2.insert_at_start(1)
llist2.insert_at_start(2)
llist2.insert_at_start(5)
llist2.insert_at_start(10)
sort_linked_list(llist2)

merged_list = merge_sorted_lists(llist, llist2)
merged_list.print_list()
