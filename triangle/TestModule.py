'''
Created on Sep 17, 2013

@author: acer
'''
import unittest
import DemoModule
from DemoModule import checkTriangle
import math


'''
Phai co 2 loai test: Test dung va test sai
'''

class Test(unittest.TestCase):



    def test_checkTriangle_wrongInput(self):
        self.assertEqual("Fail Input", DemoModule.checkTriangle(-4, 5, 6))
          
    def test_checkTriangle_wrongInput_1(self):
        self.assertEqual("Fail Input", DemoModule.checkTriangle(10^40, 5, 6))
          
    def test_checkTriangle_wrongInput_2(self):
        self.assertEqual("Fail Input", DemoModule.checkTriangle(-10^40+3, -10^40+4, -10^40+5))  
        
    def test_checkTriangle_wrongInput_3(self):
        self.assertEqual("Fail Input", checkTriangle("hello", 4, 5))
        
    def test_checkTriangle_Khongphaitamgiac(self):
        self.assertEqual("khong phai tam giac", checkTriangle(1, 5, 10))
        
    def test_checkTriangle_Tamgiacthuong(self):
        self.assertEqual("tam giac thuong", checkTriangle(3, 5, 6))
        
    def test_checkTriangle_Tamgiaccan(self):
        self.assertEqual("tam giac can", checkTriangle(3, 3, 5))
        
    def test_checkTriangle_Tamgiacvuongcan(self):
        self.assertEqual("tam giac vuong can", checkTriangle(2, 2, math.sqrt(8)))
        
    def test_checkTriangle_Tamgiacdeu(self):
        self.assertEqual("tam giac deu", checkTriangle(5, 5, 5))
        
    
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()