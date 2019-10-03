from Number1 import *

def formation (x):
    k = LinkList()
    s = len(x)
    while s != 0:
        c = ord(x[s - 1]) - ord ('0')
        k.add(c,-1)
        s = s- 1
    return k
  
def sum (f, s):
    flag = 0
    l = LinkList()
    fcurr = f.first
    scurr = s.first
    while fcurr != None and scurr != None:
        t = fcurr.value + scurr.value + flag
        if t < 10:
            flag = 0
            l.add(t, -1)
        else:
            flag = 1
            l.add(t % 10, -1)
        fcurr = fcurr.next
        scurr = scurr.next
    while fcurr != None:
        t = fcurr.value + flag
        if t < 10:
            flag = 0
            l.add(t, -1)
        else:
            flag = 1
            l.add(t % 10, -1)
        fcurr = fcurr.next
    while scurr != None:
        t = scurr.value + flag
        if t < 10:
            flag = 0
            l.add(t, -1)
        else:
            flag = 1
            l.add(t % 10, -1)
        scurr = scurr.next
    if flag == 1:
        l.add(flag, -1)
    return l

            
#пример для проверки функций
a = input()
b = input()
l = LinkList()
m = LinkList()
l = formation(a)
m = formation(b)
c = sum (m,l)
print ("первое число в виде списка")
print (l)
print ("второе число в виде списка")
print (m)
print ("сумма списков: ")
print (c)
