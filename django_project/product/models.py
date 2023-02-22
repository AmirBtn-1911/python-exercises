from django.db import models

# Create your models here.

class subCategories(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, null=False, blank=True, verbose_name="کلید اصلی",
                             name="id_subcat")
    name = models.CharField(max_length=25, verbose_name="نام زیر دسته بندی")


class Categories(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, null=False, blank=True, verbose_name="کلید اصلی", name="id_cat")
    name = models.CharField(max_length=25, verbose_name="نام دسته بندی")
    parent = models.ForeignKey(subCategories, verbose_name="زیر دسته بندی", on_delete=models.CASCADE)


class products(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, null=False, blank=True, verbose_name="کلید اصلی", name="id_product")
    name = models.CharField(max_length=25, verbose_name="نام محصول")
    count = models.PositiveSmallIntegerField(verbose_name="تعداد محصول")
    price = models.PositiveBigIntegerField(verbose_name="قیمت محصول")
    des = models.TextField(verbose_name="توضیحات")
    cat = models.ForeignKey(Categories, verbose_name="دسته بندی", on_delete=models.CASCADE)

    # class Meta:
    #     verbose_name="pro"
