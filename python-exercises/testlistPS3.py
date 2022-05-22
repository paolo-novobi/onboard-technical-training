import unittest
import listPS3

class listPS3Test1(unittest.TestCase):
    def testcommonlist(self):
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.assertEqual(listPS3.listfunc3(a,b),[1,2,3,5,8,13])

class listPS3Test2(unittest.TestCase):
    def testcommonlist1(self):
        a = []
        b = []
        self.assertEqual(listPS3.listfunc3(a,b),[])

class listPS3Test3(unittest.TestCase):
    def testcommonlist1(self):
        a = [1,2,4,4,8]
        b = [1,2,2,4,12]
        self.assertEqual(listPS3.listfunc3(a,b),[1,2,4])

class listPS3Test4(unittest.TestCase):
    def testcommonlist1(self):
        a = [1,2,4,4,8]
        b = [5,7,9,11]
        self.assertEqual(listPS3.listfunc3(a,b),[])


class listPS3TestSuite(unittest.TestSuite):
    def suite():
        theSuite = unittest.TestSuite()
        theSuite.AddTest(listPS3Test1)
        theSuite.AddTest(listPS3Test2)
        theSuite.AddTest(listPS3Test3)
        theSuite.AddTest(listPS3Test4)
        return theSuite

if __name__ == '__main__':
    unittest.main()
