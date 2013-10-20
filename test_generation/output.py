'''
Created on Oct 6, 2013

@author: DUONGHM
'''
import re
import operator
from random import randint
import unittest
import inspect
import input

#lines = doc.split('\n')
#for line in lines:
#    print '@'+line.strip()+'@'
    
class MyRange:
    def __init__(self, minValue, maxValue):
        self.minValue = minValue
        self.maxValue = maxValue
    def isInRange(self, value):
        return self.minValue <= value and self.maxValue>=value
    def getRandomValue(self):
        return randint(self.minValue, self.maxValue)    
        
class VariableInformation:
    def __init__(self, varName, listValidRange):
        self.varName = varName
        self.listValidRange = listValidRange        
    def getListValidValue(self):
        lst = []
        for l in self.listValidRange:
            lst.append(l.getRandomValue())
        return lst
    def getInvalidValue(self):
        return self.listValidRange[len(self.listValidRange)-1].maxValue + 1
    def getListTestValue(self):
        lst = []
        for l in self.listValidRange:
            lst.append(l.getRandomValue())
        lst.append(self.listValidRange[len(self.listValidRange)-1].maxValue + 1)
        return lst

class InputInformation:
    def __init__(self, lstVarInfor):
        self.lstVarInfor = lstVarInfor
    def getListTestCase(self):
        lst = [[]]
        for l in self.lstVarInfor:            
            lst = compose2List(lst, l.getListTestValue())
        return lst
    
def isOverlapRange(range1, range2):
    """Two 2 must be sorted by minValue"""
    return (range1.minValue<=range2.maxValue) and (range1.maxValue>=range2.minValue)  
    
def isInclude(range1, range2):
    """Two 2 must be sorted by minValue"""
    return range1.isInRange(range2.minValue) and range1.isInRange(range2.maxValue)

def isInvalidRange(range1, range2):
    """Two 2 must be sorted by minValue"""
    return isOverlapRange(range1, range2) or isInclude(range1, range2)  

def isValidListRange(listRange):
    listRange.sort(key=operator.attrgetter("minValue"), reverse=False)
    for i in range(0, len(listRange)-1):
        if isInvalidRange(listRange[i], listRange[i+1]):
            return False
    return True

def parseString(line):
    if re.match(r'^(\w)+: (\[(\d+);(\d+)\])*$', line):
        varName = re.search('(\w+):', line).group(1)
        rangeTuples = re.findall('\[(\d+);(\d+)\]', line)
        listRange = []
        for r in rangeTuples:            
            value1 = int(r[0])
            value2 = int(r[1])
            listRange.append(MyRange(min(value1,value2), max(value1, value2)))
        if not isValidListRange(listRange):
            raise 'wrong input'
        else:
            return VariableInformation(varName, listRange)
    else:
        raise 'invalid format'

def compose2List(lst1, lst2):
    lst = []        
    for l1 in lst1:
        for l2 in lst2:
            lst += [l1 +[l2]]
    return lst

def initInputInforFromDoc(doc, func):
    lines = doc.split('\n')
    funcArgs = inspect.getargspec(func)[0]
    lst = []    
    for line in lines:
        if line.strip() <> '':
            varInfor = parseString(line.strip())            
            lst.insert(funcArgs.index(varInfor.varName), varInfor)        
    return InputInformation(lst)

# doc = input.main.__doc__
# info = initInputInforFromDoc(doc, input.main)
# print info.getListTestCase()

class MyTest(unittest.TestCase):
    pass
 
def test_generator(a, b):
    def test(self):
        self.assertEqual(a, b) 
    return test
 
if __name__ == '__main__':
    doc = input.main.__doc__
    inputInfor = initInputInforFromDoc(doc, input.main)
    testCases = inputInfor.getListTestCase()    
    i = 0
    for t in testCases:        
        test_name = 'test_%d' % i
        i = i+1       
        test = test_generator(input.main(*t), "")        
        setattr(MyTest, test_name, test)
    unittest.main()