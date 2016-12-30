import unittest
from try_collections import LastUpdateOrderedDict
from collections import OrderedDict


class testLastUpdateOrderedDict(unittest.TestCase):
    def setUp(self):
        #d = LastUpdateOrderedDict(3)
        pass

    def tearDown(self):
        pass

    def test_init(self):
        d = LastUpdateOrderedDict(3)
        self.assertTrue(isinstance(d, dict))
        self.assertTrue(isinstance(d, OrderedDict))

    def test_setitem(self):
        d = LastUpdateOrderedDict(3)
        d['1'] = 1
        self.assertEqual(d['1'], 1)


if __name__ == '__main__':
    unittest.main()
