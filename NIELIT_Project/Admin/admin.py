from django.contrib import admin
from .models import Admin,Employee,Role

# Register your models here.
admin.site.register(Admin)
admin.site.register(Employee)
admin.site.register(Role)