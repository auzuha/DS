from utils import SinglyLL,createSinglyLL,printLL


def main():
    pos = 1
    data = 99
    head = createSinglyLL(1,2,3,4,5,6,7)
    printLL(head)
    temp = head
    cnt = 0
    newNode = SinglyLL(data)

    if pos == 0:
        newNode.next = head
        head = newNode
    else:
        while cnt < pos - 1:
            temp = temp.next
            cnt += 1
        
        if temp.next is None:
            temp.next = newNode
        else:
            newNode.next = temp.next.next
            temp.next = newNode
    printLL(head)
main()