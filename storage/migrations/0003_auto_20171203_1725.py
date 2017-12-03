# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 17:25
from __future__ import unicode_literals

from django.db import migrations


def add_data(apps, schema_editor):
    Category = apps.get_model("storage", "Category")
    fruits = Category.objects.create(name="fruits")
    shaurmas = Category.objects.create(name="shaurmas")

    Product = apps.get_model('storage', 'Product')
    Product.objects.create(name="apple",
                           category=fruits,
                           pictureURL="https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Red_Apple.jpg/200px-Red_Apple.jpg",
                           price=29,
                           description="Tasty apple. Очень вкусное яблочко дорогой. Купи не пожалешь. Вся семья ест радуется какие вкусные яболчки. Ай объедениеце. Больше бери дорогой. Ай дорогой можешь ещё к брату зайти там от такие арбузы. Я те скидочку сразу выпишу, а дорогой?")
    Product.objects.create(name="stawberry",
                           category=fruits,
                           pictureURL="https://smokeit-live.storage.googleapis.com/upload/www.smokeitlondon.com/other/strawberry-10ml-e-juice.jpg",
                           price=9,
                           description="Forests strawberry")
    Product.objects.create(name="WaterMelon",
                           category=fruits,
                           pictureURL="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Watermelon_slices_BNC.jpg/220px-Watermelon_slices_BNC.jpg",
                           price=11,
                           description="Tasty waterMelon")
    Product.objects.create(name="bigShaurma",
                           category=shaurmas,
                           pictureURL="http://www.cookforfun.ru/images/shaurma/mainphoto-big.jpg",
                           price=10,
                           description="Big shava")
    Product.objects.create(name="smallShaurma",
                           category=shaurmas,
                           pictureURL="https://www.menu.am/resources/default/img/restaurant_products/big/1449757626,3754.jpeg",
                           price=5,
                           description="Small shava")


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0002_auto_20171203_1724'),
    ]

    operations = [
        migrations.RunPython(add_data),
    ]