'''
Created on Sep 24, 2013

@author: acer
'''
import unittest
import triangle
from test.test_typechecks import Integer
import math


class Test(unittest.TestCase):


    def test_checkTriangle_wrongInput_minA(self):
        self.assertEqual("Fail Input", Triangle.detect_triangle(0, 3, 5))
        
    def test_checkTriangle_wrongInput_minB(self):
        self.assertEqual("Fail Input", Triangle.detect_triangle(3, 0, 5))
        
    def test_checkTriangle_wrongInput_minC(self):
        self.assertEqual("Fail Input", Triangle.detect_triangle(3, 5, 0))
        
    def test_checkTriangle_Khongphaitamgiac_minAplus(self):
        self.assertEqual("khong phai tam giac", Triangle.detect_triangle(0.1, 3, 5))
        
    def test_checkTriangle_Khongphaitamgiac_minBplus(self):
        self.assertEqual("khong phai tam giac", Triangle.detect_triangle(3, 0.1, 5))
        
    def test_checkTriangle_Khongphaitamgiac_minCplus(self):
        self.assertEqual("khong phai tam giac", Triangle.detect_triangle(3, 5, 0.1))
        
    def test_checkTriangle_Khongphaitamgiac_maxA(self):
        self.assertEqual("khong phai tam giac", Triangle.detect_triangle(pow(2,32)-1, 3, 5))
        
    def test_checkTriangle_Khongphaitamgiac_maxB(self):
        self.assertEqual("khong phai tam giac", Triangle.detect_triangle(3, pow(2,32)-1, 5))
        
    def test_checkTriangle_Khongphaitamgiac_maxC(self):
        self.assertEqual("khong phai tam giac", Triangle.detect_triangle(3, 5, pow(2,32)-1))    
        
    def test_checkTriangle_Khongphaitamgiac_maxAminus(self):
        self.assertEqual("khong phai tam giac", Triangle.detect_triangle(pow(2,32)-1-1, 3, 5))
        
    def test_checkTriangle_Khongphaitamgiac_maxBminus(self):
        self.assertEqual("khong phai tam giac", Triangle.detect_triangle(3, pow(2,32)-1-1, 5))
        
    def test_checkTriangle_Khongphaitamgiac_maxCminus(self):
        self.assertEqual("khong phai tam giac", Triangle.detect_triangle(3, 5, pow(2,32)-1-1))
            
    def test_checkTriangle_wrongInput_A_string(self):
        self.assertEqual("Fail Input", Triangle.detect_triangle("pow(2,32)-1-1", 3, 5))
        
    def test_checkTriangle_wrongInput_B_string(self):
        self.assertEqual("Fail Input", Triangle.detect_triangle(3, "pow(2,32)-1-1", 5))
        
    def test_checkTriangle_wrongInput_C_string(self):
        self.assertEqual("Fail Input", Triangle.detect_triangle(3, 5, "pow(2,32)-1-1"))
                
    def test_checkTriangle_wrongInput_A_boolean(self):
        self.assertEqual("Fail Input", Triangle.detect_triangle(True, 3, 5))
        
    def test_checkTriangle_wrongInput_B_boolean(self):
        self.assertEqual("Fail Input", Triangle.detect_triangle(3, True, 5))
    
    def test_checkTriangle_wrongInput_C_boolean(self):
        self.assertEqual("Fail Input", Triangle.detect_triangle(3, 5, True))
                    
    def test_checkTriangle_wrongInput_A_None(self):
        self.assertEqual("Fail Input", Triangle.detect_triangle(None, 3, 5))
        
    def test_checkTriangle_wrongInput_B_None(self):
        self.assertEqual("Fail Input", Triangle.detect_triangle(3, None, 5))
        
    def test_checkTriangle_wrongInput_C_None(self):
        self.assertEqual("Fail Input", Triangle.detect_triangle(3, 5, None))
        
    def test_checkTriangle_wrongInput_A_Tuple(self):
        self.assertEqual("Fail Input", Triangle.detect_triangle((2,5), 3, 5))
        
    def test_checkTriangle_wrongInput_B_Tuple(self):
        self.assertEqual("Fail Input", Triangle.detect_triangle(3, (1,2), 5))
        
    def test_checkTriangle_wrongInput_C_Tuple(self):
        self.assertEqual("Fail Input", Triangle.detect_triangle(3, 5, (1,2)))
        
    def test_checkTriangle_Khongphaitamgiac_midA(self):
        self.assertEqual("khong phai tam giac", Triangle.detect_triangle((0+pow(2,32)-1)/2, 3, 5))
        
    def test_checkTriangle_Khongphaitamgiac_midB(self):
        self.assertEqual("khong phai tam giac", Triangle.detect_triangle(3, (0+pow(2,32)-1)/2, 5))
        
    def test_checkTriangle_Khongphaitamgiac_midC(self):
        self.assertEqual("khong phai tam giac", Triangle.detect_triangle(3, 5, (0+pow(2,32)-1)/2))
        
    def test_checkTriangle_Tamgiacdeu_maxA_maxB_maxC(self):
        self.assertEqual("tam giac deu", Triangle.detect_triangle(pow(2,32)-1,pow(2,32)-1,pow(2,32)-1))
        
    def test_checkTriangle_Tamgiaccan_maxA_maxB_midC(self):
        self.assertEqual("tam giac can", Triangle.detect_triangle( pow(2,32)-1 , pow(2,32)-1 , (pow(2,32)-1)/2) )
        
    def test_checkTriangle_Tamgiacvuongcan_midA_midB_maxC(self):
        self.assertEqual("tam giac vuong can", Triangle.detect_triangle( (pow(2,32)-1)/math.sqrt(2) , (pow(2,32)-1)/math.sqrt(2) , pow(2,32)-1) )
            
    def test_checkTriangle_Tamgiacdeu_2(self):
        self.assertEqual("tam giac deu", Triangle.detect_triangle("1.1","1.1","1.1"))
            
    def test_checkTriangle_Tamgiacvuong_1(self):
        self.assertEqual("tam giac vuong", Triangle.detect_triangle("3.0","4.0","5.0"))    
    
	
	def test_checkTriangle_wrongInput(self):
        self.assertEqual("Fail Input", Triangle.detect_triangle(-4, 5, 6))
          
    def test_checkTriangle_wrongInput_1(self):
        self.assertEqual("Fail Input", Triangle.detect_triangle(pow(10, 40), 5, 6))
          
    def test_checkTriangle_wrongInput_2(self):
        self.assertEqual("Fail Input", Triangle.detect_triangle(-pow(10, 40)+3, -pow(10, 40)+4, -pow(10, 40)+5))  
        
    def test_checkTriangle_wrongInput_3(self):
        self.assertEqual("Fail Input", detect_triangle("hello", 4, 5))
        
    def test_checkTriangle_Khongphaitamgiac(self):
        self.assertEqual("khong phai tam giac", detect_triangle(1, 5, 10))
        
    def test_checkTriangle_Tamgiacthuong(self):
        self.assertEqual("tam giac thuong", detect_triangle(3, 5, 6))
        
    def test_checkTriangle_Tamgiaccan(self):
        self.assertEqual("tam giac can", detect_triangle(3, 3, 5))
        
    def test_checkTriangle_Tamgiacvuongcan(self):
        self.assertEqual("tam giac vuong can", detect_triangle(2, 2, math.sqrt(8)))
        
    def test_checkTriangle_Tamgiacdeu(self):
        self.assertEqual("tam giac deu", detect_triangle(5, 5, 5))
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()