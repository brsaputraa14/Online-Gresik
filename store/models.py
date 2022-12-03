from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50,blank=False, null=False)
    img = models.ImageField(upload_to='category',blank=True, null=True)
    parent = models.ForeignKey('self',related_name="childern",on_delete = models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created',]
        verbose_name_plural = 'Categories'    

class Product(models.Model):
    name = models.CharField(max_length=200, blank=False , null = False )
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name = 'category')
    tipe = models.ForeignKey(Category,blank=True,null=True,on_delete=models.CASCADE,related_name = 'tipe')
    preview_des = models.CharField(max_length=255, verbose_name='short description')
    description = models.TextField(verbose_name ='description')
    img = models.ImageField(upload_to='product',blank=True, null=True)
    price = models.FloatField()
    old_price = models.FloatField(default=0.000,blank=True,null=True)
    stok = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(200)])
    status = models.BooleanField(default=True)
    slug = models.SlugField(default=name)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.stok}"

    class Meta:
        ordering = ['-created']

    def get_product_url(self):
        return reverse('product_details', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)    

class ProductImages(models.Model):
    product =  models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product-gallery')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product.name)

class VariationManager(models.Manager):
    def jeniss(self):
        return super(VariationManager, self).filter(variation='jenis')


VARIATION_TYPE = {
    ('jenis','jenis')
}

class VariationValue(models.Model):
    variation = models.CharField(max_length=100, choices=VARIATION_TYPE)
    name = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    price = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    objects = VariationManager()

    def __str__(self):
        return self.name
    