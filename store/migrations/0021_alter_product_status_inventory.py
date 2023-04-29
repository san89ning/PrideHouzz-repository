# Generated by Django 4.2 on 2023-04-29 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_product_quantity_alter_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('waitingapproval', 'Waiting approval'), ('deleted', 'Deleted'), ('draft', 'Draft'), ('active', 'Active')], default='active', max_length=50),
        ),
        migrations.CreateModel(
            name='inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='store.product')),
            ],
            options={
                'verbose_name_plural': 'inventories',
            },
        ),
    ]