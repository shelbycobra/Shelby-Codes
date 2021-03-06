# Generated by Django 2.1 on 2018-08-07 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180807_0743'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.Category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(default='0000000'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='0000000', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='0000000', max_length=255),
        ),
    ]
