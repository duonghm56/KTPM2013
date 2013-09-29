'''
Created on Sep 24, 2013

@author: acer
'''
import unittest
import triangle
import math
from decimal import Decimal


class Test(unittest.TestCase):

    def test_checkTriangle_wrongInput_A_string(self):
        self.assertEqual("Fail Input", triangle.detect_triangle("pow(2,32)-1-1", 3, 5))
        
    def test_checkTriangle_wrongInput_B_string(self):
        self.assertEqual("Fail Input", triangle.detect_triangle(3, "pow(2,32)-1-1", 5))
        
    def test_checkTriangle_wrongInput_C_string(self):
        self.assertEqual("Fail Input", triangle.detect_triangle(3, 5, "pow(2,32)-1-1"))
                
    def test_checkTriangle_wrongInput_A_boolean(self):
        self.assertEqual("Fail Input", triangle.detect_triangle(True, 3, 5))
        
    def test_checkTriangle_wrongInput_B_boolean(self):
        self.assertEqual("Fail Input", triangle.detect_triangle(3, True, 5))
    
    def test_checkTriangle_wrongInput_C_boolean(self):
        self.assertEqual("Fail Input", triangle.detect_triangle(3, 5, True))
                    
    def test_checkTriangle_wrongInput_A_None(self):
        self.assertEqual("Fail Input", triangle.detect_triangle(None, 3, 5))
        
    def test_checkTriangle_wrongInput_B_None(self):
        self.assertEqual("Fail Input", triangle.detect_triangle(3, None, 5))
        
    def test_checkTriangle_wrongInput_C_None(self):
        self.assertEqual("Fail Input", triangle.detect_triangle(3, 5, None))
        
    def test_checkTriangle_wrongInput_A_Tuple(self):
        self.assertEqual("Fail Input", triangle.detect_triangle((2,5), 3, 5))
        
    def test_checkTriangle_wrongInput_B_Tuple(self):
        self.assertEqual("Fail Input", triangle.detect_triangle(3, (1,2), 5))
        
    def test_checkTriangle_wrongInput_C_Tuple(self):
        self.assertEqual("Fail Input", triangle.detect_triangle(3, 5, (1,2)))
        
    def test_checkTriangle_wrongInput_A_List(self):
        self.assertEqual("Fail Input", triangle.detect_triangle([1,5], 3, 5))
        
    def test_checkTriangle_wrongInput_B_List(self):
        self.assertEqual("Fail Input", triangle.detect_triangle(3, [1,5], 5))
        
    def test_checkTriangle_wrongInput_C_List(self):
        self.assertEqual("Fail Input", triangle.detect_triangle(3, 5, [1,5]))

    def test_checkTriangle_wrongInput_minA(self):
        self.assertEqual("Fail Input", triangle.detect_triangle(0, 3, 5))
        
    def test_checkTriangle_wrongInput_minB(self):
        self.assertEqual("Fail Input", triangle.detect_triangle(3, 0, 5))
        
    def test_checkTriangle_wrongInput_minC(self):
        self.assertEqual("Fail Input", triangle.detect_triangle(3, 5, 0))
        
    def test_checkTriangle_wrongInput_maxA(self):
        self.assertEqual("Fail Input", triangle.detect_triangle(2**32-1+10**-6, 3, 5))
        
    def test_checkTriangle_wrongInput_maxB(self):
        self.assertEqual("Fail Input", triangle.detect_triangle(3, 2**32-1+10**-6, 5))
        
    def test_checkTriangle_wrongInput_maxC(self):
        self.assertEqual("Fail Input", triangle.detect_triangle(3, 5, 2**32-1+10**-6))
        
                
    def test_checkTriangle_Khongphaitamgiac_minAplus(self):
        self.assertEqual("khong phai tam giac", triangle.detect_triangle(10**-6, 3, 5))
        
    def test_checkTriangle_Khongphaitamgiac_minBplus(self):
        self.assertEqual("khong phai tam giac", triangle.detect_triangle(3, 10**-6, 5))
        
    def test_checkTriangle_Khongphaitamgiac_minCplus(self):
        self.assertEqual("khong phai tam giac", triangle.detect_triangle(3, 5, 10**-6))
        
    def test_checkTriangle_Khongphaitamgiac_maxA(self):
        self.assertEqual("khong phai tam giac", triangle.detect_triangle(2**32-1, 3, 5))
        
    def test_checkTriangle_Khongphaitamgiac_maxB(self):
        self.assertEqual("khong phai tam giac", triangle.detect_triangle(3, 2**32-1, 5))
        
    def test_checkTriangle_Khongphaitamgiac_maxC(self):
        self.assertEqual("khong phai tam giac", triangle.detect_triangle(3, 5, 2**32-1))    
        
    def test_checkTriangle_Khongphaitamgiac_maxAminus(self):
        self.assertEqual("khong phai tam giac", triangle.detect_triangle(2**32-1-1, 3, 5))
        
    def test_checkTriangle_Khongphaitamgiac_maxBminus(self):
        self.assertEqual("khong phai tam giac", triangle.detect_triangle(3, 2**32-1-1, 5))
        
    def test_checkTriangle_Khongphaitamgiac_maxCminus(self):
        self.assertEqual("khong phai tam giac", triangle.detect_triangle(3, 5, 2**32-1-1))
            
    def test_checkTriangle_Khongphaitamgiac_midA(self):
        self.assertEqual("khong phai tam giac", triangle.detect_triangle((0+pow(2,32)-1)/2, 3, 5))
        
    def test_checkTriangle_Khongphaitamgiac_midB(self):
        self.assertEqual("khong phai tam giac", triangle.detect_triangle(3, (0+pow(2,32)-1)/2, 5))
        
    def test_checkTriangle_Khongphaitamgiac_midC(self):
        self.assertEqual("khong phai tam giac", triangle.detect_triangle(3, 5, (0+pow(2,32)-1)/2))
        
        
    def test_checkTriangle_Tamgiacthuong_minAplus(self):
        self.assertEqual("tam giac thuong", triangle.detect_triangle(10**-6, 2, 2+10**-6/2))
            
    def test_checkTriangle_Tamgiacthuong_minBplus(self):
        self.assertEqual("tam giac thuong", triangle.detect_triangle(2, 10**-6, 2+10**-6/2))
            
    def test_checkTriangle_Tamgiacthuong_minCplus(self):
        self.assertEqual("tam giac thuong", triangle.detect_triangle(2, 2+10**-6/2, 10**-6))    
        
    def test_checkTriangle_Tamgiacthuong_maxA(self):
        self.assertEqual("tam giac thuong", triangle.detect_triangle(2**32-1, 2**32-3, 2**32-3.5))
            
    def test_checkTriangle_Tamgiacthuong_maxB(self):
        self.assertEqual("tam giac thuong", triangle.detect_triangle(2**32-3, 2**32-1, 2**32-3.5))
            
    def test_checkTriangle_Tamgiacthuong_maxC(self):
        self.assertEqual("tam giac thuong", triangle.detect_triangle(2**32-3, 2**32-3.5, 2**32-1))
            
    def test_checkTriangle_Tamgiacthuong_midA(self):
        self.assertEqual("tam giac thuong", triangle.detect_triangle(2, 2**32-3, 2**32-4))
            
    def test_checkTriangle_Tamgiacthuong_midB(self):
        self.assertEqual("tam giac thuong", triangle.detect_triangle(2**32-3, 2, 2**32-4))
            
    def test_checkTriangle_Tamgiacthuong_midC(self):
        self.assertEqual("tam giac thuong", triangle.detect_triangle(2**32-3, 2**32-4, 2))    
        
        
    def test_checkTriangle_Tamgiacvuong_minA_minB_minC(self):  
        self.assertEqual("tam giac vuong", triangle.detect_triangle(3*10**-6, 4*10**-6, 5*10**-6))
        
    def test_checkTriangle_Tamgiacvuong_midA_midB_midC(self):  
        self.assertEqual("tam giac vuong", triangle.detect_triangle(3,4,5))
        
        
    def test_checkTriangle_Tamgiaccan_minA_minB_minC(self):  
        self.assertEqual("tam giac can", triangle.detect_triangle(10**-3, 10**-3, 10**-3/2))
        
    def test_checkTriangle_Tamgiaccan_midA_midB_midC(self):  
        self.assertEqual("tam giac can", triangle.detect_triangle(2,2,3))
        
    def test_checkTriangle_Tamgiaccan_maxA_maxB_maxC(self):  
        self.assertEqual("tam giac can", triangle.detect_triangle(2**32-1,2**32-1,2**32-2))
    
    
    def test_checkTriangle_Tamgiacvuongcan_minA_minB_minC_1(self):  
        self.assertEqual("tam giac vuong can", triangle.detect_triangle(10**-6, 10**-6, 10**-6*math.sqrt(2)))
        
    def test_checkTriangle_Tamgiacvuongcan_minA_minB_minC_2(self):  
        self.assertEqual("tam giac vuong can", triangle.detect_triangle(10**-6, 10**-6*math.sqrt(2), 10**-6))
        
    def test_checkTriangle_Tamgiacvuongcan_minA_minB_minC_3(self):  
        self.assertEqual("tam giac vuong can", triangle.detect_triangle(10**-6*math.sqrt(2), 10**-6, 10**-6))
        
    def test_checkTriangle_Tamgiacvuongcan_midA_midB_midC_1(self):  
        self.assertEqual("tam giac vuong can", triangle.detect_triangle(2, 2, math.sqrt(8)))
        
    def test_checkTriangle_Tamgiacvuongcan_midA_midB_midC_2(self):  
        self.assertEqual("tam giac vuong can", triangle.detect_triangle(2, math.sqrt(8), 2))
        
    def test_checkTriangle_Tamgiacvuongcan_midA_midB_midC_3(self):  
        self.assertEqual("tam giac vuong can", triangle.detect_triangle(math.sqrt(8), 2, 2))
        
    def test_checkTriangle_Tamgiacvuongcan_maxA_maxB_maxC(self):  
        self.assertEqual("tam giac vuong can", triangle.detect_triangle( (2**32-1) / (2**0.5), (2**32-1) / (2**0.5), 2**32-1))
    
    
    def test_checkTriangle_Tamgiacdeu_minA_minB_minC(self):
        self.assertEqual("tam giac deu", triangle.detect_triangle( 10**-6 , 10**-6, 10**-6))
        
    def test_checkTriangle_Tamgiacdeu_midA_midB_midC(self):
        self.assertEqual("tam giac deu", triangle.detect_triangle( 3 , 3, 3))
        
    def test_checkTriangle_Tamgiacdeu_maxA_maxB_maxC(self):
        self.assertEqual("tam giac deu", triangle.detect_triangle( 2**32-1 , 2**32-1, 2**32-1))
   
   
            
    def test_checkTriangle_Tamgiacdeu_2(self):
        self.assertEqual("tam giac deu", triangle.detect_triangle("1.1","1.1","1.1"))
            
    def test_checkTriangle_Tamgiacvuong_1(self):
        self.assertEqual("tam giac vuong", triangle.detect_triangle("3.0","4.0","5.0"))    
    
    
                         
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()