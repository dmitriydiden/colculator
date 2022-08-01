'''
41. Напишите программу вычисления арифметического выражения заданного строкой. 
Используйте операции +,-,/,*. приоритет операций стандартный.
*Пример:*
2+2 => 4;
1+2*3 => 7;
1-2*3 => -5;
- Добавьте возможность использования скобок, меняющих приоритет операций.
*Пример:*
1+2*3 => 7;
(1+2)*3 => 9;
'''
import re
from tkinter import W
text = '1+1+5'
list = []
for line in text:
    list.append(line)
result = 0
result = result + int(list[0])
print(result)
i=1    
while i < len(list):
    if list[i] == '+':
        result+=int(list[i+1])
        i=i+2
        print(i, result)
    elif list[i] == '-':
        result-=int(list[i+1])
        i=i+2
print(result)

  
        


#list = re.split('\+|\-|\/|\*', text)
#list = re.split('\|', text)
print(list)