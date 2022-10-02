from asyncio.windows_events import NULL
from utils import SinglyLL, createSinglyLL, printLL

def main():
    head = createSinglyLL(1,2,3,4,5)
    printLL(head)
    data = 99
    temp = head
    newNode = SinglyLL(data)
    while temp.next.next is not None:
        temp = temp.next
    temp.next = newNode
    printLL(head)

main()