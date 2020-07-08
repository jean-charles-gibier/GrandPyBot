import unittest

class TestBasics4validationCI(unittest.TestCase):
    """
    Test de validtation du dispositif Circle-ci
    pour obtenir un check de départ
    """
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()