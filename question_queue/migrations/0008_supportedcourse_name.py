# Generated by Django 4.1.2 on 2022-11-08 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("question_queue", "0007_queuequestion_attending"),
    ]

    operations = [
        migrations.AddField(
            model_name="supportedcourse",
            name="name",
            field=models.TextField(blank=True, null=True),
        ),
    ]