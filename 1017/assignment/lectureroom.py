
time=[]
n= int(input())
for i in range(n):
    s, t= input().split(' ')
    st=[s, t]
    time.append(st)

time.sort(key = lambda x: x[1])


finish_time = [time[0][1]]
k=0 ##강의실

for i in range(1,n):
    flag = False
    for j in range(k+1):
        if time[i][0] >=finish_time[j]:
            finish_time[j] = time[i][1]
            flag = True
            break
    if not flag:    
        k += 1
        finish_time.append(time[i][1])

print(k+1)
