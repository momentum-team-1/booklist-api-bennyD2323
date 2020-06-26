from django.db import models
from django.contrib.auth.models import AbstractUser


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
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="book_users")

    status = model.CharField(max_length=7), choices=BookStatusChoice.choices, default=BookStatusChoice.to_read)

    title = model.textField(max_length=100),


class Notes(models.Model):
    created_at = models.DateTimeField(auto_now_add=True),
    body = model.CharField(max_length=200),
    page_num = model.charfield(max_length=10),