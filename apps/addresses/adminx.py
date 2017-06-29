from .models import Address
import xadmin


class AddressAdmin(object):
    list_display = ['address', 'date_time']

xadmin.site.register(Address, AddressAdmin)
