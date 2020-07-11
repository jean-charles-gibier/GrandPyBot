"""
(Future) tests that mocks API behaviour
{
   "candidates": [
      {
         "formatted_address": "Paris, France",
         "geometry": {
            "location": {
               "lat": 48.856614,
               "lng": 2.3522219
            },
            "viewport": {
               "northeast": {
                  "lat": 48.9021449,
                  "lng": 2.4699208
               },
               "southwest": {
                  "lat": 48.815573,
                  "lng": 2.224199
               }
            }
         }
      }
   ],
   "status": "OK"
}"""

import unittest

class TestGooglePlaceAPIAnswser(unittest.TestCase):
    """
    Test de validtation gg
    """
    def test_dummy(self):
        """
        Just test the test
        """
        self.assertEqual(True, True)
