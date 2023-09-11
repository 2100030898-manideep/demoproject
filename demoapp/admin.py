from django.contrib import admin

from .models import Employee,Registration,Department

admin.site.register(Employee)
admin.site.register(Registration)
admin.site.register(Department)