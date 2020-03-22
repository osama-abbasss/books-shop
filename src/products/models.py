from django.db import models
from django.utils.text import slugify

LABLE_CHOICES =(
('new','new'),
('best_saler', 'best_saler'),
)


class Product(models.Model):
    author = models.CharField(max_length = 250)
    title = models.CharField(max_length = 120, unique=True)
    description = models.TextField()
    current_price = models.FloatField()
    old_price = models.FloatField(blank=True, null=True)
    date_of_publication = models.DateField()
    lable = models.CharField(max_length=50, choices=LABLE_CHOICES)
    related_product = models.ManyToManyField("self")
    slug = models.SlugField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField('Category')
    related_product = models.ManyToManyField('self', blank=True, null=True)
    stock = models.IntegerField(default=1)
    def __str__(self):
        return self.title

    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)

        elif self.slug != slugify(self.title):
            self.slug = slugify(self.title)
        super().save()


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image   = models.ImageField(upload_to = 'books/')
    front   = models.BooleanField(default=False)
    back    = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.title



class Category(models.Model):
    category   = models.CharField(max_length =120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category
