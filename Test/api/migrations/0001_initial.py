# Generated by Django 2.1.3 on 2018-12-10 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Metadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SKU', models.IntegerField(null=True)),
                ('NAME', models.CharField(default='', max_length=40)),
                ('LOCATION', models.CharField(default='', max_length=40)),
                ('DEPARTMENT', models.CharField(max_length=45)),
                ('CATEGORY', models.CharField(default='', max_length=40)),
                ('SUBCATEGORY', models.CharField(default='', max_length=40)),
            ],
            options={
                'managed': True,
            },
        ),
    ]