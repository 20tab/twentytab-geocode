from django.conf import settings
import requests


class GeocodeClient(object):

    def __init__(self, address, data={}):
        self.address = address
        self._prepare_address()
        self.data = data

    def _prepare_address(self):
        splitted = [w for w in self.address.split(' ') if w]
        self.address = u"+".join(splitted)

    def _data_join(self):
        qs_list = [u'{}={}'.format(k, v) for k, v in self.data.items()]
        return u'&'.join(qs_list)

    def get(self):
        url_api = settings.GMAPS_API_URL
        self.data[u'key'] = settings.GMAPS_API_KEY
        self.data[u'address'] = self.address

        path = u'{}/{}?{}'.format(
            url_api,
            settings.GMAPS_API_TYPE,
            self._data_join()
        )

        return requests.get(path)