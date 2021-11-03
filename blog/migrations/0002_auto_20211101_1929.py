# Generated by Django 3.2.8 on 2021-11-01 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='advertiser',
            field=models.CharField(choices=[('شخصی', 'شخصی'), ('مشاور املاک', 'مشاور املاک')], default=(('شخصی', 'شخصی'), ('مشاور املاک', 'مشاور املاک')), max_length=30, verbose_name='آگهی دهنده'),
        ),
        migrations.AlterField(
            model_name='article',
            name='property_contract',
            field=models.CharField(choices=[('-------', '-------'), ('اجاره', 'اجاره'), ('خرید', 'خرید')], default=(('-------', '-------'), ('اجاره', 'اجاره'), ('خرید', 'خرید')), max_length=20, verbose_name='نوع آگهی'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(help_text='عنوان ادرس سایت بهتر است مانند عنوان آگهی باشد (به ازای هر فاصله - بزنید)', max_length=200, unique=True, verbose_name='آدرس سایت'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='آدرس دسته بندی'),
        ),
    ]
