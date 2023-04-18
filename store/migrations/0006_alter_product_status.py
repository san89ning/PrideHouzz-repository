# Generated by Django 4.2 on 2023-04-18 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('deleted', 'Deleted'), ('waitingapproval', 'Waiting approval'), ('active', 'Active')], default='active', max_length=50),
        ),
    ]
