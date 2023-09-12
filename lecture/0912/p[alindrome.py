pal = "asdffdsa"
text1=[]
text2=[]
print(pal[1])


print(len(pal)/2)


for i in range(int(len(pal)/2)):
    text1.append(pal[i])

print(text1)


for j in range(len(pal)-1, int(len(pal)/2), -1):

    text2.append(pal[j])

    print(text2)
