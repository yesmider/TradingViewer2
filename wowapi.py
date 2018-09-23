import requests

class WOWAPI:
    def __init__(self,api_key=dfdfca2x4bsf2cnxqkx3utrjn9w5yw2h,region='TW'):
        self.api_key=api_key
        self.region = region
        self.Session = requests.Session()

    def __url_get(self,url):
        res = self.Session.get(url)
        if res.status_code == 200:
            return res
        else:
            raise ConnectionError(res.status_code)

    def __locale(self,locale):
        if locale == '':
            if self.region == 'US':
                return 'en_US'
            elif self.region == 'TW':
                return 'zh_TW'
            elif self.region == 'EU':
                return ''
            elif self.region == 'KR':

    def auction_api(self,locale=''):


