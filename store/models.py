from django.db import models
from cloudinary.models import CloudinaryField  # ← استيراد CloudinaryField


class Category(models.Model):
    name = models.CharField("اسم التصنيف", max_length=100)
    slug = models.SlugField("المعرف الفريد", unique=True)

    class Meta:
        verbose_name = "تصنيف"
        verbose_name_plural = "التصنيفات"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name="التصنيف"
    )
    name = models.CharField("اسم المنتج", max_length=200)
    description = models.TextField("الوصف")
    price = models.DecimalField("السعر", max_digits=10, decimal_places=2)
    image = CloudinaryField("صورة المنتج")  # ← التغيير هنا
    created_at = models.DateTimeField("تاريخ الإضافة", auto_now_add=True)
    available = models.BooleanField("متوفر", default=True)

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"

    def __str__(self):
        return f"{self.name} - {self.category.name}"
