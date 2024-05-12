from django.contrib import admin

from user.models import MasterUser, ClientUser

# Register your models here.
admin.site.register(MasterUser)
admin.site.register(ClientUser)
