from django.contrib import admin

# Register your models here.
from .models import RandomUser

admin.site.register(RandomUser)