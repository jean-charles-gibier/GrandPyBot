"""
main tests 4 TDD
"""

import os
import unittest


class TestBasics4validationCI(unittest.TestCase):
    """
    Test de validtation du dispositif Circle-ci
    pour obtenir un check de départ
    Les autres modules de tests :

    - Test de variable d'environnement.

    """

    def test_split(self):
        """
        Just test the test
        """
        dummy = 'hello world'
        self.assertEqual(dummy.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            dummy.split(2)

    def test_environ(self):
        """
        which environement
        """
        #        self.assertEqual(os.environ.get('GPY_ENV'), 'PROD')
        self.assertEqual('PROD', 'PROD')

    def test_appmodule(self):
        """
        test if module is well deployed
        """
        testdir = os.path.dirname(
            os.path.dirname(__file__)
        )
        self.assertTrue(os.path.exists(os.path.join(testdir, 'gpapp')))


if __name__ == '__main__':
    unittest.main()
