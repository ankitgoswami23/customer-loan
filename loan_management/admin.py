from django.contrib import admin
from loan_management import models

# Register your models here.
admin.site.register(models.Customer)
admin.site.register(models.Branch)
admin.site.register(models.CustomerAddress)
