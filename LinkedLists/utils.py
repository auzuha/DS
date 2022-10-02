from re import A


class SinglyLL:
    def __init__(self, data):
        self.data = data
        self.next = None


class DoublyLL:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

def createSinglyLL(*args):
    """
    Create singly LL and return pointer to head 
    """
    arr = []
    for i in range(len(args)):
        arr.append(SinglyLL(args[i]))
    for i in range(len(arr)-1):
        arr[i].next = arr[i+1]
    return arr[0]


def createDoublyLL(*args):
    """
    Create doublt LL and return pointer to head
    """
    arr = []
    for i in range(len(args)):
        arr.append(DoublyLL(args[i]))
    for i in range(1,len(args) - 1):
        arr[i].next = arr[i+1]
        arr[i].prev = arr[i-1]
    return arr[0]



def printLL(head):
    while head:
        if head.next is None:
            print(head.data)
        else:
            print(head.data,"-> ",end="")
        head = head.next