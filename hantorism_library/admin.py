from django.contrib import admin

from common_hantorism.models import HantorismBook, HantorismRentBook, HantorismUser, HantorismOverflow

admin.site.register(HantorismBook)
admin.site.register(HantorismRentBook)
admin.site.register(HantorismUser)
admin.site.register(HantorismOverflow)

