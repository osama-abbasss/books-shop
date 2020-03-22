from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.conf import settings
User = settings.AUTH_USER_MODEL

GENDER_CHOICES = (
('male', 'male'),
('female', 'female')
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null= True)
    gender = models.CharField(max_length= 6, choices = GENDER_CHOICES)
    address = models.CharField(max_length=200,blank=True, null= True)

    class Meta:
        verbose_name = 'user profile'
        verbose_name_plural = 'users profiles'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)

        elif self.slug != slugify(self.user.username):
            self.slug = slugify(self.user.username)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username



def create_user_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user = kwargs['instance'])


post_save.connect(create_user_profile, sender=User)
