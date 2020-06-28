from django.contrib import admin
from rest_framework.authtoken.models import Token
from .models import User, Book
# Register your models here.

admin.site.register(Book)
admin.site.register(User)