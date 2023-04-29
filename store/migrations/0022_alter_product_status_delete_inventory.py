# Generated by Django 4.2 on 2023-04-29 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_alter_product_status_inventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('deleted', 'Deleted'), ('waitingapproval', 'Waiting approval'), ('draft', 'Draft')], default='active', max_length=50),
        ),
        migrations.DeleteModel(
            name='inventory',
        ),
    ]