from django.contrib import admin
from .models import platillo
from .models import chef
from .models import compra
# Register your models here.
admin.site.register(compra)
admin.site.register(platillo)
admin.site.register(chef)
