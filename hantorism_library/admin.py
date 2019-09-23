from django.contrib import admin

from common_hantorism.models import HantorismBook, HantorismRentBook, HantorismUser

admin.site.register(HantorismBook)
admin.site.register(HantorismRentBook)
admin.site.register(HantorismUser)
