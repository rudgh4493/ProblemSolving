def binary_search(a, left, right, K):
    if right >= left:
        mid = (left + right) // 2
        if a[mid] == K:
            return True

        elif a[mid] > K:
            return binary_search(a, left, mid-1, K)

        else:
            return binary_search(a, mid+1, right, K)

    else:
        return False

input_list = [10, 20, 25, 35, 45, 55, 60, 75, 85, 90]
n = len(input_list)
print('55 탐색:', binary_search(input_list, 0, n-1, 55))
print('50 탐색:', binary_search(input_list, 0, n-1, 90))
