# Generated by Django 3.1.14 on 2022-11-24 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_cart_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(1, 'Pesanan sedang diajukan'), (2, 'Pesanan sedang dikemas'), (2, 'Pesanan sedang diantar'), (3, 'Pesanan sudah sampai'), (4, 'Pesanan telah diambil')], default='1'),
        ),
    ]