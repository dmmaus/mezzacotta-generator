
# Python Key:
# 0319e6d5ac637fdc02db5a4d823fe7f7

import flickrapi
import urllib
from PIL import Image
import random


class FlickrGettr():
    def __init__(self):
        self.api_key = u'0319e6d5ac637fdc02db5a4d823fe7f7'
        with open('..\\flickr-secret.txt') as sf:
            self.api_secret = sf.readline()

        self.flickr = flickrapi.FlickrAPI(self.api_key, self.api_secret, cache=True)

    def GetKeyword(self, keyword):

        photos = self.flickr.walk(
            text=keyword,
            tag_mode='any',
            tags=keyword,
            extras='url_c',
            per_page=100,
            sort='date'
        )

        urls = []

        for i, photo in enumerate(photos):
            url = photo.get('url_c')
            urls.append(url)
            if i > 10:
                break;

        if len(urls) == 0:
            return None

        idx = random.randrange(len(urls))
        if urls[idx] == None:
            return None

        urllib.urlretrieve(urls[idx], '..\\001.jpg')

        return '001.jpg'


if __name__ == '__main__':
    print 'Starting'

    flickr = FlickrGettr()
    print flickr.GetKeyword('extending')