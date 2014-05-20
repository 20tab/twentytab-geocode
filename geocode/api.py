import requests


class GeocodeClient(object):

    url = "https://maps.googleapis.com/maps/api/geocode"
    api_type = "json"

    def __init__(self, address, key, data={}, url=None, api_type=None):
        self.address = address
        self._prepare_address()
        self.key = key
        self.data = data
        if url:
            self.url = url
        if api_type:
            self.api_type = api_type

    def _prepare_address(self):
        splitted = [w for w in self.address.split(' ') if w]
        self.address = u"+".join(splitted)

    def _data_join(self):
        qs_list = [u'{}={}'.format(k, v) for k, v in self.data.items()]
        return u'&'.join(qs_list)

    def uri(self):
        self.data[u'key'] = self.key
        self.data[u'address'] = self.address

        return u'{}/{}?{}'.format(
            self.url,
            self.api_type,
            self._data_join()
        )

    def get(self):
        return requests.get(self.uri())