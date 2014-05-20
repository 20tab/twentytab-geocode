from appconf import AppConf
from django.conf import settings

print "CANE"

class GeocodeConf(AppConf):
    GMAPS_API_URL = "https://maps.googleapis.com/maps/api/geocode"
    GMAPS_API_TYPE = "json"

    def configure_gmaps_api_url(self, value):
        if not getattr(settings, 'GMAPS_API_URL', None):
            self._meta.holder.GMAPS_API_URL = value
            return value
        return getattr(settings, 'GMAPS_API_URL')

    def configure_gmaps_api_type(self, value):
        if not getattr(settings, 'GMAPS_API_TYPE', None):
            self._meta.holder.GMAPS_API_TYPE = value
            return value
        return getattr(settings, 'GMAPS_API_TYPE')