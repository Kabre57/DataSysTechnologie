from django.db import models

# Create your models here.

class products(models.Model):
    name = models.CharField (max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10000 ,decimal_places=3)
    image = models.ImageField(upload_to='images', blank=True )
    slug = models.SlugField(null=True)
    actif = models.BooleanField(default=True)
    
    class Meta :
        verbose_name = ("product")
        verbose_name_plural = ("products")
        
    def __str__(self):
        return self.name