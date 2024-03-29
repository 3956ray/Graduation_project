# Generated by Django 4.0.4 on 2022-04-30 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0008_admininfo_alter_hospital_province'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='province',
            field=models.SmallIntegerField(choices=[(19, '内蒙古'), (32, '浙江'), (3, '重庆'), (4, '福建'), (22, '山东'), (15, '吉林'), (24, '陕西'), (20, '宁夏'), (10, '河北'), (17, '江西'), (27, '台湾'), (12, '黑龙江'), (16, '江苏'), (25, '上海'), (5, '甘肃'), (29, '西藏'), (2, '北京'), (34, '澳门'), (21, '青海'), (7, '广西'), (14, '湖南'), (31, '云南'), (28, '天津'), (23, '山西'), (18, '辽宁'), (26, '四川'), (1, '安徽'), (33, '香港'), (11, '河南'), (30, '新疆'), (6, '广东'), (8, '贵州'), (13, '湖北'), (9, '海南')], verbose_name='省份'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.SmallIntegerField(choices=[(1, '男'), (2, '女')], verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='name',
            field=models.CharField(max_length=32, verbose_name='用户名'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='password',
            field=models.CharField(max_length=64, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='userType',
            field=models.SmallIntegerField(choices=[(2, '保险公司'), (3, '医药供应商'), (1, '医院'), (4, '医疗设备供应商'), (5, '管理员')], max_length=32, verbose_name='用户种类'),
        ),
    ]
