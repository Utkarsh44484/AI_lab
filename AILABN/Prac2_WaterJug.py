def AinB():
    x = int(input("Enter capacity of A-"))
    y = int(input("Enter capacity of B-"))
    A = x
    B = 0
    s = 0
    n = int(input("Enter final state of A-"))
    if n > x or n < 0:
        print("Invalid State entered..")
        return
    print("State - [", A, ",", B, "]")
    while A != n:
        if A == 0:
            A = x

        elif B == y:
            B = 0

        else:
            if A > y - B:
                A = A - (y - B)
                B = y
            else:
                B = B + A
                A = 0
        s += 1
        print("State - [", A, ",", B, "]")
        if A == n:
            break
    print("Total steps required - ", s)
    return s


def BinA():
    x = int(input("Enter capacity of A-"))
    y = int(input("Enter capacity of B-"))
    A = 0
    B = y
    s = 0
    n = int(input("Enter final state of B-"))
    if n > y or n < 0:
        print("Invalid State entered..")
        return
    print("State - [", A, ",", B, "]")
    while B != n:
        if B == 0:
            B = y

        elif A == x:
            A = 0

        else:
            if B > x - A:
                B = B - (x - A)
                A = x
            else:
                A = A + B
                B = 0
        s += 1
        print("State - [", A, ",", B, "]")
        if B == n:
            break
    print("Total steps required - ", s)
    return s


def main():
    m = AinB()
    n = BinA()
    print("Difference between steps is ", abs(m-n))


main()
