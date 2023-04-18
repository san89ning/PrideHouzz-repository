# Generated by Django 4.2 on 2023-04-18 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_product_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name_plural': 'OrderItems'},
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('waitingapproval', 'Waiting approval'), ('deleted', 'Deleted'), ('draft', 'Draft')], default='active', max_length=50),
        ),
    ]
