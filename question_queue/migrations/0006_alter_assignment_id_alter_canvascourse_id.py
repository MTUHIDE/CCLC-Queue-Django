# Generated by Django 4.1.1 on 2022-10-17 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("question_queue", "0005_alter_queuequestion_answered_by"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assignment",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="canvascourse",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
