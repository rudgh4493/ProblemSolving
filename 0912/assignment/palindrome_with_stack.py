string = input("문자열을 입력하시오: ")


stack=[]

for i in range(len(string)):
               stack.append(string[i])
               palindrome = True

for i in range(len(string)):
               if stack.pop()!=string[i]:
                   palindrome = False
                   
makePalindrome= string + string[::-1]      

if palindrome==True:
    print('Yes\n'+ string)
else:
    print('No\n'+ makePalindrome)
