from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name='태그명')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'fastcampus_tag'
        verbose_name = '유송커뮤니티 태그'
        verbose_name_plural = '유송커뮤니티 태그'