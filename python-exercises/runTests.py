import os, unittest

class Tests():

    def suite(self): #Function stores all the modules to be tested
        modules_to_test = []
        test_dir = os.listdir('.')
        for test in test_dir:
            if test.startswith('test') and test.endswith('.py'):
                modules_to_test.append(test.rstrip('.py'))

        alltests = unittest.TestSuite()
        for module in map(__import__, modules_to_test):
            module.testvars = ["variables you want to pass through"]
            alltests.addTest(unittest.findTestCases(module))
        return alltests

if __name__ == '__main__':
    MyTests = Tests()
    unittest.main(defaultTest='MyTests.suite')

#if __name__ == '__main__':
#    MyTests = Tests()
#    log_file = 'log_file.txt'
#    f = open(log_file, "w")
#    runner = unittest.TextTestRunner(f)
#    unittest.main(defaultTest='MyTests.suite', testRunner=runner)
