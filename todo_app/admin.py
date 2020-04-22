from django.contrib import admin

# Register your models here.
from .models import todoitems

admin.site.register(todoitems)