"""
Imiter une réponse HTTP
Ex :tests that mocks GG API behaviour
"""
import sys
import urllib.request
from io import BytesIO
import json
sys.path.append('..')
sys.path.append('.')

class TestGooglePlaceAPIAnswser:
    """
    Test de validtation gg
    """

    def test_dummy(self):
        """
        Just test the test
        """
        assert (True == True)

    def test_gg_simple_std_answer(self, monkeypatch):
        """
        test requete
        input = 'Paris'
        """
        import gpapp.google_api as script
        results = [
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
            }]
        def mockreturn(arg):
            return BytesIO(json.dumps(results).encode())

        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        gg_test = script.GoogleApi()
        mocked_answer = gg_test.findplacefromtext('Paris')
        assert mocked_answer == results



    def test_wiki_simple_std_answer(self, monkeypatch):
        """
        test wiki à retravailler
        input = 'Paris'
        """
        import gpapp.wiki_media_api as script
        results = "Big text sample sur Paris"

        def mockreturn(arg1, arg2):
            return results

        monkeypatch.setattr(script.WikiMediaApi, 'opensearch', mockreturn)
        wiki_test = script.WikiMediaApi()
        mocked_answer = wiki_test.opensearch('Paris')
        assert mocked_answer == results
