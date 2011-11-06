from django.contrib import admin
from models import Hosting

class HostingAdmin(admin.ModelAdmin):
    list_display = ('name','description','add_date','update_date',)

admin.site.register(Hosting,HostingAdmin)
