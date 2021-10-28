from django.contrib.postgres.fields import ArrayField
from django.db import models


class Product(models.Model):
    title = models.CharField(verbose_name='タイトル', max_length=40)
    content = models.TextField(verbose_name='本文', blank=True, null=True)
    img1 = models.ImageField(verbose_name='写真1')
    img2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    img3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    img4 = models.ImageField(verbose_name='写真4', blank=True, null=True)
    code_url = models.URLField(verbose_name='コードURL', blank=True, null=True)
    url = models.URLField(verbose_name='URL', blank=True, null=True)
    tags = ArrayField(models.CharField(max_length=20), verbose_name="タグ", blank=True, null=True)
    created_at = models.DateField(verbose_name='作成日', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Product'

    def __str__(self):
        return self.title
