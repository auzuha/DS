from utils import SinglyLL, createSinglyLL

def main():
    numNodes = 0
    head = createSinglyLL(1,2,3,4,5,6,7,8)

    temp = head
    while temp.next:
        numNodes += 1
        temp = temp.next
    numNodes += 1
    middle = numNodes // 2 + 1
    cnt = 0
    temp = head
    while cnt < middle - 1:
        temp = temp.next
        cnt += 1
    print(temp.data)
    

main()

