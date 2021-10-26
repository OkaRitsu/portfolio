from django.db import models


class Product(models.Model):
    title = models.CharField(verbose_name='タイトル', max_length=40)
    content = models.TextField(verbose_name='本文', blank=True, null=True)
    img1 = models.ImageField(verbose_name='写真1')
    img2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    img3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    img4 = models.ImageField(verbose_name='写真4', blank=True, null=True)
    created_at = models.DateField(verbose_name='作成日', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = 'Product'

    def __str__(self):
        return self.title
