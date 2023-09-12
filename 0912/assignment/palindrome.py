string= input('문자열을 입력하세요:')

for i in range(len(string)//2):
    if string[i] != string[-1-i]:
        palindrome = False
    else:
        palindrome = True

makePalindrome= string + string[::-1]        
        
if palindrome==True:
    print('Yes\n'+ string)
else:
    print('No\n'+ makePalindrome)
