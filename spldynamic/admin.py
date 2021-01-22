from django.contrib import admin
from .models import product,productadmin
from .models import people,peopleadmin

# Register your models here.
admin.site.register(product,productadmin)
admin.site.register(people,peopleadmin)
