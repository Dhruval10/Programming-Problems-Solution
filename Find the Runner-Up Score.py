if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = sorted(arr)
    
    for i in reversed(range((len(arr)))):
        if arr[i] != arr[i-1]:
            print(arr[i-1])
            break
