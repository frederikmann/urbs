import sys
import unittest

sys.path.append('../urbs')

loader = unittest.TestLoader()
testSuite = loader.discover('test_urbs',pattern='test*.py')
testRunner = unittest.TextTestRunner(verbosity=2)
testRunner.run(testSuite)