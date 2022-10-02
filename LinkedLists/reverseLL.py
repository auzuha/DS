from utils import SinglyLL, createSinglyLL, printLL



def reverse(head):
    if head:
        reverse(head.next)
        print(head.data,"-> ",end="")

def main():
    head = createSinglyLL(1,2,3,4,5)
    reverse(head)


main()