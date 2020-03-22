from django.db import models
from django.conf import settings
from django_countries.fields import CountryField

User = settings.AUTH_USER_MODEL

ADDRESS_TYPE_CHOICES = (
('S', 'shipping'),
('B', 'billing')
)

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 60, null=True, blank=True)
    last_name = models.CharField(max_length = 60, null=True, blank=True)
    country =  CountryField()
    zip_code = models.CharField(max_length = 15, null=True, blank=True)
    address = models.CharField(max_length = 150, null=True, blank=True)
    address_type = models.CharField(max_length=1, choices= ADDRESS_TYPE_CHOICES)
    phone_num = models.CharField(max_length = 15, null=True, blank=True)
    default_address = models.BooleanField(default=False)


    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = 'Addresses'
