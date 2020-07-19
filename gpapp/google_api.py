"""
All the stuff for fetching info on gg API
"""
import json
import os
import time
import urllib.request
from gpapp import constant


class GoogleApi:
    """
     main GG class
    """

    def findplacefromtext(self, text):
        """
        main GG class
        gets standard adress place + coordinates
        """
        try:
            gg_text = urllib.parse.quote(text)
            gg_key_api_find_place = os.getenv('GG_KEY_API_FIND_PLACE')
            print("Key GG API_FIND_PLACE :'{}'".format(gg_key_api_find_place))
            gg_url = constant.URL_API_FIND_PLACE_GG.format(
                gg_text,
                gg_key_api_find_place)
            response = urllib.request.urlopen(gg_url)
            if response is not None:
                return json.loads(response.read().decode("utf8"))
        except urllib.error.HTTPError as err:
            print("Request error '{}', sleeping 1s".format(err.code))
            time.sleep(1)
        return {
            "candidates": [
                {
                    "formatted_address": "North pole",
                    "geometry":
                        {
                            "location":
                                {"lat": 90,
                                 "lng": 0
                                 }
                        }
                }
            ], "status": "KO"}
