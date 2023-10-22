# simple linked list implementation
class ListNode():
    val = 0
    next = None

    def __init__(self, v, n=None):
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
    temp = ll
    count = 0
    while count < pos - 1:
        count += 1
        temp = temp.next
    new_node = ListNode(elem, temp.next)
    temp.next = new_node
    return ll


def remove_element_at(ll, pos):
    # your code here
    return None


# push adds an element to the list
def push(ll, elem):
    # if ll is none, return new ListNode
    temp = ll
    if temp == None:
        return ListNode(elem, None)
    while temp != None and temp.next != None:
        temp = temp.next
    temp.next = ListNode(elem, None)
    return ll


# pop removes the last element in the list
def pop(ll):
    # if no elements in list, return None

    # if only 1 element in list, return None
    temp = ll
    if temp == None or temp.next == None:
        return None
    while temp.next.next != None:
        temp = temp.next
    temp.next = None
    return ll


if __name__ == "__main__":
    
    ll = ListNode(0, None)
    print_ll(ll) # [0]

    temp = pop(ll)
    print_ll(temp)
    pop(temp)

    push(temp, 0)

    ll = push(ll, 5) # ll = [0, 5]
    ll = push(ll, 10) # ll = [0, 5, 10]

    print_ll(ll) # [0, 5, 10]

    ll = pop(ll) # ll = [0, 5]

    ll = push(ll, 7) # ll = [0, 5, 7]

    print_ll(ll) # ll = [0, 5, 7]
    
    # add element at creates a new List Node and add is at the specified index
    # example: add_element_at(ll, 3, 1) --> [0, 3, 5, 7]
    print_ll(add_element_at(ll, 3, 1))
    