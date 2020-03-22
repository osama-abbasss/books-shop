from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    order_code = models.CharField(max_length=25)
    subject = models.CharField(max_length=25)
    message = models.TextField()

    def __str__(self):
        return self.subject
