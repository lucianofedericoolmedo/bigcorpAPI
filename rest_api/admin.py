from django.contrib import admin
from rest_api.models.employee import Employee, Office, Department

admin.site.site_header = "BigCorp Api Backoffice"
admin.site.site_title = "Backoffice Portal"
admin.site.index_title = "Bienvenidos a BigCorp Api"

admin.site.register(Employee)
admin.site.register(Office)
admin.site.register(Department)
