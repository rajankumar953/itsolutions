# Generated by Django 4.2 on 2023-04-30 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=122)),
                ('lname', models.CharField(max_length=122)),
                ('username', models.CharField(max_length=122)),
                ('password', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
            ],
        ),
    ]
