import random
#점찍기
N= 100
a = []
random.seed(0)
i=0

while i<N:
    x_coord = random.randint(0, 2000)
    y_coord = random.randint(0, 1000)
    if[x_coord, y_coord] not in a:
        a.append([x_coord, y_coord])
        i+=1



import math

def get_dist(a, b):  # 두 점 사이의 거리를 구하는 함수
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)


def get_min(arr, start, end):
    if start == end:  # 점이 하나인 경우, 최대값 반환
        return 0

    if end - start == 1:  # 점이 두 개인 경우, 두 점 사이의 거리 반환
        return get_dist(arr[start], arr[end])

    mid = (start + end) // 2  # 중간 지점 계산

    print(f'start={start}, mid={mid}, end={end}')
    # 왼쪽 절반과 오른쪽 절반을 각각 재귀적으로 호출하여 최소 거리를 구함
    min_dist = min(get_min(arr, start, mid), get_min(arr, mid, end))

    # 가운데 점(mid)을 기준으로 거리가 min_dist보다 작은 점들을 candidates 리스트에 추가
    candidates = []
    for i in range(start, end+1):
        if (arr[mid][0] - arr[i][0])**2 < min_dist:
            candidates.append(arr[i])

    # candidates 리스트를 y좌표를 기준으로 정렬
    candidates.sort(key=lambda x: x[1])

    # candidates 리스트 내에서 최소 거리를 구함
    for i in range(len(candidates)-1):
        for j in range(i+1, len(candidates)):
            print(candidates, f'min_dist = {min_dist}')
            # y좌표 차이가 min_dist보다 작은 경우에만 최소 거리 계산
            if (candidates[i][1] - candidates[j][1])**2 < min_dist:
                min_dist = min(min_dist, get_dist(candidates[i], candidates[j]))
            else:
                break

    return min_dist

print(get_min(a, 0, len(a)-1))

