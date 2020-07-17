"""
All the stuff for fetching info on gg API
"""
import json
import time
import urllib.request
from gpapp import constant



class GoogleApi:
    """
     main GG class
    """
    def __init__(self):
        """
        Standard init
        """
        pass

    def findplacefromtext(self, text):
        """
        main GG class
        gets standard adress place + coordinates
        """
        try:
            gg_text = urllib.parse.quote(text)
            gg_url = constant.URL_API_GG_FMT.format(gg_text, constant.KEY_API_GG)
            response = urllib.request.urlopen(gg_url)
            if response is not None:
                return json.loads(response.read().decode("utf8"))
        except urllib.error.HTTPError as e:
            print("Request error '{}', sleeping 5s".format(e.code))
            time.sleep(5)
        return {"candidates": [{"formatted_address": ""}], "status": "KO"}

