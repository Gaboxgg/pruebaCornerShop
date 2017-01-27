from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Shopper)
admin.site.register(Actividad)
admin.site.register(Feedbacks)
