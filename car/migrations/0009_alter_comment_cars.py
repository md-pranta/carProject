# Generated by Django 4.2.7 on 2023-12-16 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0008_remove_carmodel_user_alter_comment_cars_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='cars',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='car.carmodel'),
        ),
    ]
