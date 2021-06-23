from urllib.request import urlopen
import json

class ShadowData():
    
    
    def __init__(self, url):
      
    
        self._url   = url
        self._data  = None
        self.show()
        
    def show(self):
       
        openUrl = urlopen(self._url)
        if (openUrl.getcode() == 200):
            self._data = openUrl.read()
        else:
            raise ConnectionError("Received an error {} from server, cannot retrieve results ".format(str(openUrl.getcode())))
        return self
    
    def getData(self):
    
        return self._data
    
    def parseJson(self):
      
        return json.loads(self.getData())
