from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField('Category name', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Brand(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='catbrand')
    name = models.CharField('Brand name', max_length=30)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


class Prod(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brandprod', null=True)
    name = models.CharField('Prod name', max_length=50)
    price = models.IntegerField('Prod price')
    img = models.ImageField('Prod image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Prod'
        verbose_name_plural = 'Prods'


# class Nout(models.Model):
#     name = models.CharField('Nout name', max_length=50)
#     price = models.IntegerField('Nout price')
#     img = models.ImageField('Nout image', upload_to='media')

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = 'Nout'
#         verbose_name_plural = 'Nouts'


# class Watch(models.Model):
#     name = models.CharField('Watch name', max_length=50)
#     price = models.IntegerField('Watch price')
#     img = models.ImageField('Watch image', upload_to='media')

#     def __str__(self):
#         return self.name


