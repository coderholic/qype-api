"""
Simple Qype API wrapper. See http://apidocs.qype.com/ for details.
Ben Dowling - ben@coderholic.com

Example usage:

    q = Qype('YOUR_CONSUMER_KEY')
    
    places = q.get_locations(53.5532,9.95805)
    
    place_id = '197584'
    place_details = q.get_details(place_id)
    place_reviews = q.get_reviews(place_id)    

The MIT License

Copyright (c) 2010 Ben Dowling
 
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
 
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
 
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import httplib
import simplejson as json

class Qype(object):
    def __init__(self, api_key, timeout = 10):
        self.api_key = api_key
        self.connection = httplib.HTTPConnection("api.qype.com", timeout = timeout)
    
    def _request(self, url):
        try:
            self.connection.request("GET", url)
            response = self.connection.getresponse()
            data = response.read()
            return json.loads(data)
        except:
            return {'error': 'Problem with request'}
            
    def get_locations(self, lat, lon, radius = 2):
        return self._request( "http://api.qype.com/v1/positions/%s,%s/places.json?in_category=609&radius=%s&consumer_key=%s" % (lat, lon, radius, self.api_key))
   
    def get_details(self, place_id):
        return self._request("http://api.qype.com/v1/places/%s.json?&consumer_key=%s" % (place_id, self.api_key))
  
    def get_reviews(self, place_id):
        return self._request("http://api.qype.com/v1/places/%s/reviews.json?order=date_updated&consumer_key=%s" % (place_id, self.api_key))
