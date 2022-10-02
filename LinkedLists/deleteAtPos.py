from utils import SinglyLL,printLL,createSinglyLL


def main():
    head = createSinglyLL(1,2,3,4,5)
    pos = 2
    cnt = 0
    temp = head

    printLL(head)

    while cnt < pos - 1:
        temp = temp.next
        cnt += 1
    temp.next = temp.next.next

    printLL(head)
main()