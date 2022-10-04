# Generated by Django 4.1.1 on 2022-10-04 19:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("question_queue", "0004_question_hidden_queuequestion"),
    ]

    operations = [
        migrations.AlterField(
            model_name="queuequestion",
            name="answered_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]