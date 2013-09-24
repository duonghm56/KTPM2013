'''
Created on Sep 17, 2013

@author: acer
'''
from test.test_typechecks import Integer
import math

'''
Ham check tam giac. So int tu 0 -> 2^32-1
Nhan dang : 
+ Khong phai tam giac
+ Tam giac thuong
+ Tam giac vuong
+ Tam giac can
+ Tam giac vuong can
+ Tam giac deu
'''

'''
Check dau vao, check mien gia tri, check ma doc
Xu ly
Xuat du lieu
'''

'''
Kiem tra dau vao:
+ Kiem tra so bien dau vao
+ Kiem tra kieu du lieu dau vao
'''
def checkInput(a):
    return a>0 and a<2^32-1 and ((type(a) is int) or (type(a) is float)) 

def checkTamgiacDeu(a,b,c):
    return a==b and b==c and c==a

def checkTamgiacCan(a,b,c):
    return a==b or b==c or c==a

def isEqual(a, b):
    return math.fabs(a-b) < pow(10, -9)

def checkTamgiacvuong(a,b,c):        
    return isEqual(a*a + b*b, c*c) or isEqual(b*b + c*c, a*a) or isEqual(a*a + c*c, b*b) 

def checkTamgiac(a,b,c):
    return (a+b>c) and (a+c>b) and (b+c>a)

def checkTriangle(a, b, c):
    'return (a+b>c) and (a+c>b) and (b+c>a) and (a>0) and (b>0) and (c>0)'
    if checkInput(a) and checkInput(b) and checkInput(c) :        
        if checkTamgiac(a, b, c):
            if checkTamgiacDeu(a, b, c):
                return "tam giac deu"
            elif checkTamgiacCan(a, b, c) and checkTamgiacvuong(a, b, c):
                return "tam giac vuong can"
            elif checkTamgiacCan(a, b, c):
                return "tam giac can"
            elif checkTamgiacvuong(a, b, c):
                return "tam giac vuong"
            else:
                return "tam giac thuong"
            
        else:
            return "khong phai tam giac"
    else:
        return "Fail Input"


'print (math.pow(math.sqrt(8),2) - (2*2 + 2*2))'
'print (8 == 8.0)'
