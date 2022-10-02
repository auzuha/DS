class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



def createLL(*args):
    arr = []
    for i in range(len(args)):
        arr.append(Node(args[i]))
    for i in range(len(arr)-1):
        arr[i].next = arr[i+1]
    return arr[0]

def printLL(head):
    while head:
        if head.next is None:
            print(head.data)
        else:
            print(head.data,"-> ",end="")
        head = head.next