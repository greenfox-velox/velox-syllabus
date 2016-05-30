import unittest
import sys


f = open(sys.argv[1], 'w')
loader = unittest.defaultTestLoader.discover('tests/', pattern='*.py')
runner = unittest.TextTestRunner(f)
runner.run(loader)
f.close()
