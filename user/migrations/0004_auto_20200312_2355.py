# Generated by Django 3.0.4 on 2020-03-12 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200308_2151'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '유송커뮤니티 사용자', 'verbose_name_plural': '유송커뮤니티 사용자'},
        ),
        migrations.AddField(
            model_name='user',
            name='useremail',
            field=models.EmailField(default='test@gmail.com', max_length=128, verbose_name='사용자이메일'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=32, verbose_name='사용자명'),
        ),
    ]
