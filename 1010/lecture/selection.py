
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



def selection(a, low, high, k):
    pivot = partition(a, low, high)
    if k < pivot:
        return selection(a, low, pivot-1, k)
    elif k == pivot:
        return a[k]
    else:
        return selection(a, pivot+1, high, k)
    

input_list = [40,20,50,70,65,90,35,10,15,60,55,80,25,75]
K = input('(k-1) 값을 입력하라(0부터 '+ str((len(input_list)-1)) + '): ')
kth_smallest  = selection(input_list, 0, len(input_list)-1, int(K))
print('{:2}번째 작은 수는 {:2}이다.'.format(int(K)+1, kth_smallest))
