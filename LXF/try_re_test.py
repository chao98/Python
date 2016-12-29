import unittest
from try_re import simple_re


class Test_simple_re(unittest.TestCase):
    def test_phone(self):
        tc1 = {
            1: (r'^\d{3}\-\d{3,8}$', '010-123456789', False),
            2: (r'^\d{3}\-\d{3,8}$', '010-1234567', True),
        }

        n = 1
        for k, v in tc1.items():
            print(k)
            self.assertEqual(simple_re(n, v[0], v[1]), v[2])

    def test_var(self):
        pass


if __name__ == '__main__':
    unittest.main()