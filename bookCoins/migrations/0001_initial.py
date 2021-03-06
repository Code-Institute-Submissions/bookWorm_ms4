# Generated by Django 3.1.1 on 2020-09-24 19:45

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0002_auto_20200924_1945'),
        ('products', '0005_auto_20200922_2041'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderChapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=32)),
                ('grand_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chapter_orders', to='profiles.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='OrderCoin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=32)),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('street_address1', models.CharField(max_length=80)),
                ('street_address2', models.CharField(blank=True, max_length=80, null=True)),
                ('town_or_city', models.CharField(max_length=40)),
                ('county', models.CharField(blank=True, max_length=80, null=True)),
                ('postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('stripe_pid', models.CharField(default='', max_length=254)),
                ('coins', models.DecimalField(decimal_places=2, default=0, max_digits=1000)),
                ('user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='coin_orders', to='profiles.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='OrderChapterLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_no', models.CharField(default=0, editable=False, max_length=254)),
                ('book', models.CharField(max_length=254)),
                ('lineitem_total', models.DecimalField(decimal_places=2, editable=False, max_digits=6)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.chapter')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='bookCoins.orderchapter')),
            ],
        ),
    ]
