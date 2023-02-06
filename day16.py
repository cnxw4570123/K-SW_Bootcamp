def is_stack_full():
    global SIZE, stack, top
    if top >= SIZE - 1:
        return True
    return False


def is_stack_empty():
    global SIZE, stack, top
    if top == -1:
        return True
    return False


def push(data):
    global SIZE, stack, top
    if is_stack_full():
        print("stack is Full!")
        return
    top += 1
    stack[top] = data


def pop():
    global SIZE, stack, top
    if is_stack_empty():
        print("stack is Empty!")
        return
    data = stack[top]
    stack[top] = None
    top -= 1
    return data


def peek():
    global SIZE, stack, top
    if is_stack_empty():
        print("stack is Empty!")
        return None
    return stack[top]


SIZE = int(input("Stack Size : "))
stack, top = [None for _ in range(SIZE)], -1

if __name__ == "__main__":

    while True:
        menu = input("Insert(I)/Extract(E)/Verify(V)/Exit(X): ")
        if menu == "X" or menu == "x":
            break
        if menu == "I" or menu == "i":
            data = input("Input Data: ")
            push(data)
            print("Stack Status : ", stack)
        elif menu == "E" or menu == "e":
            data = pop()
            print("Extracted Data ==> ", data)
            print("Stack Status : ", stack)
        elif menu == "V" or menu == "v":
            data = peek()
            print("Top is: ", data)
            print("Stack Status: ", stack)
        else:
            print("입력이 잘못됨")

    print("프로그램 종료!")
