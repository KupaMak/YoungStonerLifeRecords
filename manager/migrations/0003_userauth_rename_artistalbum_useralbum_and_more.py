# Generated by Django 4.0.4 on 2022-05-27 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_artistdetail_studio_studiosession_payrolldetail_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAuth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('username', models.CharField(max_length=80)),
                ('password', models.CharField(max_length=40)),
                ('code_number', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='ArtistAlbum',
            new_name='UserAlbum',
        ),
        migrations.RenameModel(
            old_name='ArtistDetail',
            new_name='UserDetail',
        ),
        migrations.RenameModel(
            old_name='PayrollDetail',
            new_name='UserPayroll',
        ),
        migrations.AddField(
            model_name='managerauth',
            name='code_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
