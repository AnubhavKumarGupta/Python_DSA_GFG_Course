import sys

class FastReader:
    def __init__(self):
        self.input = sys.stdin.readline
    def next(self):
        return self.input().strip()
    def nextInt(self):
        return int(self.next())
    def nextLine(self):
        return self.input().strip()

def smallestDistancePair(arr, k):
    arr.sort()
    low = 0
    high = arr[-1] - arr[0]
    while low < high:
        mi = (low + high) // 2
        count = 0
        left = 0
        for right in range(len(arr)):
            while arr[right] - arr[left] > mi:
                left += 1
            count += right - left
        if count >= k:
            high = mi
        else:
            low = mi + 1
    return low

if __name__ == "__main__":
    fr = FastReader()
    t = fr.nextInt()
    for _ in range(t):
        n, k = fr.nextInt(), fr.nextInt()
        arr = [fr.nextInt() for _ in range(n)]
        print(smallestDistancePair(arr, k))
