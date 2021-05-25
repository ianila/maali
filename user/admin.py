from django.contrib import admin
from django.contrib.auth.models import Group

from .models import MaaliUser

admin.site.register(MaaliUser)

admin.site.unregister(Group)