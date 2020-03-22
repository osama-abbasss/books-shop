from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

class Section(models.Model):
    title = models.CharField(max_length= 30,unique=True)
    slug = models.SlugField(blank=True, null=True)
    content = RichTextField()
    image = models.FileField(upload_to='resume/')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)
        elif self.title != self.slug:
            self.slug = slugify(self.title)
        super().save()



class Comment(models.Model):
    post = models.ForeignKey('Section', on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    name = models.CharField(max_length= 30)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.email)
