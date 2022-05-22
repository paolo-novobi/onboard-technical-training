import unittest
import listPS4

class listPS4Test1(unittest.TestCase):
    def testsublist(self):
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        self.assertEqual(listPS4.listfunc4(a,1),[1,89])

class listPS4Test2(unittest.TestCase):
    def testsublist(self):
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        self.assertEqual(listPS4.listfunc4(a,5),[1, 1, 2, 3, 5,13, 21, 34, 55, 89])

class listPS4Test3(unittest.TestCase):
    def testsublist(self):
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        self.assertEqual(listPS4.listfunc4(a,6),a)

class listPS4Test4(unittest.TestCase):
    def testsublist(self):
        a = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        self.assertEqual(listPS4.listfunc4(a,5),a)

class listPS4Test5(unittest.TestCase):
    def testsublist(self):
        a = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        self.assertEqual(listPS4.listfunc4(a,6),a)

class listPS4TestSuite(unittest.TestSuite):
    def suite():
        theSuite = unittest.TestSuite()
        theSuite.AddTest(listPS4Test1)
        theSuite.AddTest(listPS4Test2)
        theSuite.AddTest(listPS4Test3)
        theSuite.AddTest(listPS4Test4)
        theSuite.AddTest(listPS4Test5)
        return theSuite

if __name__ == '__main__':
    unittest.main()
