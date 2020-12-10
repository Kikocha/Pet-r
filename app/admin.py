from django.contrib import admin

from app.models.extend_user import ExtendUser
from app.models.Pet import Pet

admin.site.register(Pet)
admin.site.register(ExtendUser)
