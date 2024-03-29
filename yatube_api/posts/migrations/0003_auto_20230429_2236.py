# Generated by Django 3.2.16 on 2023-04-29 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20230429_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='posts.group'),
        ),
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.CharField(help_text='Название группы', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(help_text='Текст публикации'),
        ),
    ]
