from django.db import models
from django.utils.text import slugify

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(default= "",  null= False, unique= True, db_index = True)

    def __str__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(args, kwargs)
    

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    imageUrl = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    isActive = models.BooleanField(default=False)
    isHome = models.BooleanField(default=False)
    slug = models.SlugField(default= "", blank= True, null= False, unique= True, db_index = True)
    categories = models.ManyToManyField(Categories)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(args, kwargs)

    def __str__(self):
        return f"{self.title}"
    

