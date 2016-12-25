from django.contrib import admin
from tutorial.resturantapi.models import Menu, MenuItem
# Register your models here.
class MenuAdmin(admin.ModelAdmin):
	list_display = ['id', 'name' ,'description', 'chef']

class MenuItemAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'menu', 'description']


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)