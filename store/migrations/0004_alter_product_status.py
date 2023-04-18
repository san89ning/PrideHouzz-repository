# Generated by Django 4.2 on 2023-04-17 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('deleted', 'Deleted'), ('waitingapproval', 'Waiting approval'), ('draft', 'Draft')], default='active', max_length=50),
        ),
    ]
