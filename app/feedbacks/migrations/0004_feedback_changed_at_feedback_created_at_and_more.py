# Generated by Django 4.0 on 2022-03-06 14:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0003_module_teacher_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='changed_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='module',
            name='changed_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='module',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='changed_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='student',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='changed_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]