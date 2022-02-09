# Generated by Django 4.0.2 on 2022-02-09 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'subjects',
            },
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('profile_pic', models.ImageField(upload_to='profile_images/')),
                ('email_address', models.EmailField(max_length=100, unique=True)),
                ('phone_number', models.CharField(max_length=100)),
                ('room_number', models.CharField(max_length=100)),
                ('subjects_taught', models.ManyToManyField(related_name='avail_subjects', to='teachers.Subjects')),
            ],
            options={
                'db_table': 'Teachers',
            },
        ),
    ]