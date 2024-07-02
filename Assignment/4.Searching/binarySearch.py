l = list(map(int, input("Enter the list -").split()))
x = int(input("Enter the element that you want to search: "))


def bs(l, x, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if l[mid] == x:
        return mid

    elif l[mid] > x:
        return bs(l, x, low, mid - 1)

    else:
        return bs(l, x, mid + 1, high)


def bsmain(l, x):
    return bs(l, x, 0, len(l) - 1)


print(bsmain(l, x))
