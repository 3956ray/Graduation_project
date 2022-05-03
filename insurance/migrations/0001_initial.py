# Generated by Django 4.0.4 on 2022-05-03 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='insurance_evaluate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance_name', models.CharField(max_length=32, verbose_name='保险公司名称')),
                ('hospital_name', models.CharField(max_length=32, verbose_name='医院名称')),
                ('score', models.IntegerField(verbose_name='评估分数')),
            ],
        ),
    ]