# simple linked list implementation
class LinkedList():
    val = 0
    next = None

    def __init__(self, v, n):
        self.val = v
        self.next = n

def print_ll(ll):
    regular_list = []
    while ll != None:
        regular_list.append(ll.val)
        ll = ll.next
    print(regular_list)


def add_element_at(ll, elem, pos):
    # you code here
    return LinkedList(-1, None)


def remove_element_at(ll, pos):
    # your code here
    return None


# push adds an element to the list
def push(ll, elem):
    # your code here
    return None


# pop removes the last element in the list
def pop(ll):
    # your code here
    return None


if __name__ == "__main__":
    
    ll = LinkedList(0, None)
    print_ll(ll) # [0]

    ll = push(ll, 5) # ll = [0, 5]
    ll = push(ll, 10) # ll = [0, 5, 10]

    print_ll(ll) # [0, 5, 10]

    ll = pop(ll) # ll = [0, 5]

    ll = push(ll, 7) # ll = [0, 5, 7]

    print_ll(ll) # ll = [0, 5, 7]
    
    # add element at creates a new List Node and add is at the specified index
    # example: add_element_at(ll, 3, 1) --> [0, 3, 5, 7]
    print_ll(add_element_at(ll, 3, 1))
    