from django.contrib import admin
from .models import Courier


class CourierAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'student_rollno', 'date_recieved', 'service')
	change_list_template = 'admin/change_list.html'
	actions = None

admin.site.site_header = 'Courier System Administration'
admin.site.site_title = 'Courier System Admin'
admin.site.register(Courier, CourierAdmin)