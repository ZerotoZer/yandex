# Generated by Django 4.0.5 on 2022-06-25 12:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ShopUnit',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(choices=[('OFFER', 'OFFER'), ('CATEGORY', 'CATEGORY')], editable=False, max_length=10)),
                ('price', models.IntegerField(null=True)),
                ('parentId', models.ForeignKey(max_length=40, null=True, on_delete=django.db.models.deletion.CASCADE, to='yanprod.category')),
            ],
        ),
    ]
