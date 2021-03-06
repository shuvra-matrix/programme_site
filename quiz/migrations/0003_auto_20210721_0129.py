# Generated by Django 3.2.5 on 2021-07-20 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_stat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('score', models.CharField(max_length=10)),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('user_id', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='otp',
            field=models.IntegerField(),
        ),
    ]
