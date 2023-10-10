
def qsort(a, low, high):
    if low < high:
        pivot = partition(a, low, high)
        qsort(a, low, pivot-1)
        qsort(a, pivot + 1, high)


def partition(a, low, high):
    pivot = a[low]
    left = low+1
    right = high
    done = False
    print(f'pivot={pivot}, a[left]={a[left]}, a[right]={a[right]}')
    while not done:
        while left <= right and a[left] <= pivot:
            left += 1
        while left <= right and pivot <= a[right]:
            right -= 1
        if right < left:
            done = True
        else:
            a[left], a[right] = a[right], a[left]
            print(f'pivot={pivot}, a[left]={a[left]}, a[right]={a[right]}')
            print(a)
        a[low], a[right] = a[right], a[low]

        print(a)
    print(f'return pivot={a[right]}')
    return right


input_list = [50,80,75,30,95,90,45,10,15,70,85,30,20,50,60,20]
print('before sort : ', input_list)
qsort(input_list, 0, len(input_list)-1)
print('after sort : ', input_list)