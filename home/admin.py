from django.contrib import admin
from home.models import Description
from home.models import Contact,news,registration,billing
# Register your models here.

admin.site.register(Contact)
admin.site.register(news)
admin.site.register(registration)
admin.site.register(billing)
