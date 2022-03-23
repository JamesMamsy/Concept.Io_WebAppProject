<<<<<<< HEAD
# Generated by Django 2.2.26 on 2022-03-14 04:23
=======
# Generated by Django 2.2.26 on 2022-03-20 21:50
>>>>>>> f88be2dc146860edd93c563b3a02b3774ae03f3c

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
=======
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
>>>>>>> f88be2dc146860edd93c563b3a02b3774ae03f3c
            name='Project',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=120, verbose_name='Title')),
                ('desc', models.CharField(max_length=300, verbose_name='Description')),
                ('cat', models.CharField(default='', max_length=300, verbose_name='Category')),
                ('tags', models.CharField(default='', max_length=300, verbose_name='Tags')),
<<<<<<< HEAD
=======
                ('likes', models.IntegerField(default=0, verbose_name='likes')),
                ('dislikes', models.IntegerField(default=0, verbose_name='dislikes')),
>>>>>>> f88be2dc146860edd93c563b3a02b3774ae03f3c
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
<<<<<<< HEAD
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rango.Project')),
=======
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('url', models.URLField()),
                ('views', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conceptio.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='conceptio.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=3000, verbose_name='Comment')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='conceptio.Project')),
>>>>>>> f88be2dc146860edd93c563b3a02b3774ae03f3c
            ],
        ),
    ]
