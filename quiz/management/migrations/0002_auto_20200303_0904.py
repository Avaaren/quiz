# Generated by Django 3.0.3 on 2020-03-03 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='management.Question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='quiz',
            field=models.ManyToManyField(db_index=True, related_name='questions', to='management.Quiz'),
        ),
    ]