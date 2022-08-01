from hashlib import shake_128
from re import I


text = '1+1*5'

list = []
list1 = []
s=''
s1 = ''
result1 = 1
for i in range(len(text)):
    if text[i] == '*' or text[i] == '/':
        s=text[i-1]+text[i]+text[i+1]
        for j in s:
            list.append(j)
        print(i)
        s1 = text[:i-1]+text[i+2:]
        for i in s1:
            list1.append(i)
        for i in range(len(list)):
            if list[1]=='*':
                result1=result1*(int(list[i])*int(list[i+2]))
            elif list[1]=='/':
                if list[i+2] != 0:
                    result1=(int(list[i])/int(list[i+2]))
                else:
                    print("Делить на 0 нельзя")
                    break
        for i in range(len(list1)):
            if list1[i] == '+':
                list1.pop(i)
                result1+=int(list[i])
            if list1[i] == '-':
                list1.pop(i)
                result1-=int(list[i])        
print(s1, list, list1, result1)



