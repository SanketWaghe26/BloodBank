from django.contrib import admin
from .models import Contact
from .models import Donor

# Register your models here.

admin.site.register(Contact)
admin.site.register(Donor)