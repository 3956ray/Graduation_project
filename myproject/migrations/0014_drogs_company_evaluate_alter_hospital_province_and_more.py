# Generated by Django 4.0.4 on 2022-05-03 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0013_insurance_evaluate_alter_hospital_province_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='drogs_company_evaluate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drogs_company_name', models.CharField(max_length=32, verbose_name='医药公司名称')),
                ('hospital_name', models.CharField(max_length=32, verbose_name='医院名称')),
                ('score', models.IntegerField(verbose_name='评估分数')),
            ],
        ),
        migrations.AlterField(
            model_name='hospital',
            name='province',
            field=models.SmallIntegerField(choices=[(31, '云南'), (9, '海南'), (24, '陕西'), (30, '新疆'), (34, '澳门'), (23, '山西'), (16, '江苏'), (1, '安徽'), (33, '香港'), (4, '福建'), (22, '山东'), (29, '西藏'), (6, '广东'), (2, '北京'), (13, '湖北'), (25, '上海'), (17, '江西'), (27, '台湾'), (3, '重庆'), (10, '河北'), (12, '黑龙江'), (32, '浙江'), (20, '宁夏'), (7, '广西'), (18, '辽宁'), (21, '青海'), (15, '吉林'), (11, '河南'), (28, '天津'), (26, '四川'), (19, '内蒙古'), (14, '湖南'), (8, '贵州'), (5, '甘肃')], verbose_name='省份'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='userType',
            field=models.SmallIntegerField(choices=[(3, '医药供应商'), (2, '保险公司'), (4, '医疗设备供应商'), (1, '医院'), (5, '管理员')], max_length=32, verbose_name='用户种类'),
        ),
    ]
