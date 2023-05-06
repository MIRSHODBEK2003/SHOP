from django.db import models


class Category(models.Model):
    parent = models.ForeignKey('Category', verbose_name="Kategoriyasi",
                               null=True, blank=True, on_delete=models.PROTECT)
    name = models.CharField(verbose_name="Kategoriya nomi", max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

class Product(models.Model):
    category = models.ForeignKey('Category', verbose_name="Kategoriyasi", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Mahsulot nomi", max_length=255)
    full_name = models.CharField(verbose_name="Mahsulotning to'liq nomi", max_length=200)
    price = models.DecimalField(verbose_name="Mahsulot narxi", max_digits=17, decimal_places=2)
    description = models.TextField(verbose_name="Mahsulot haqida ma'lumot")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"

