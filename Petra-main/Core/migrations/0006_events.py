# Generated by Django 4.2.4 on 2023-11-28 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0005_partners'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Added_Date', models.DateField(auto_now_add=True)),
                ('Name', models.CharField(max_length=100)),
                ('Date', models.DateField()),
                ('Start_Time', models.TimeField()),
                ('End_Time', models.TimeField()),
                ('Description', models.TextField()),
            ],
        ),
    ]