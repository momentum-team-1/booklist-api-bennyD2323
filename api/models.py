from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db.models import Q

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


        
class User(AbstractUser):
    date_joined = models.DateTimeField(auto_now_add=True)



class Book(models.Model):

    class BookStatusChoice(models.TextChoices):
        to_read = 'to_read'
        reading = 'reading'
        read = 'read'
        BOOK_STATUS_CHOICES = [
            (to_read, 'To Read'),
            (reading, 'Reading'),
            (read, 'Read'),
        ]
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="books"),
    status = models.CharField(max_length=100, choices=BookStatusChoice.choices, default=BookStatusChoice.to_read),
    author = models.CharField(max_length=35),
    title = models.TextField(max_length=100),


class Note(models.Model):
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE, related_name="notes")  
    created_at = models.DateTimeField(auto_now_add=True),
    body = models.CharField(max_length=500),
    page_num = models.CharField(max_length=10),