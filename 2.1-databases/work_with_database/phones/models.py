
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify



class Phone(models.Model):
    id = models.CharField(max_length=100, primary_key=True, serialize=False)
    name = models.CharField(max_length=64, verbose_name='Модель телефона')
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='', verbose_name='Изображение')
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=255, verbose_name='URL')
    pass

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('phone', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
