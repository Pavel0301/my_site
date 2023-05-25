# Generated by Django 4.2 on 2023-05-23 15:39

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Discussion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        db_index=True,
                        help_text="не более 200 символов",
                        max_length=200,
                        verbose_name="Discussion title",
                    ),
                ),
                (
                    "content",
                    ckeditor.fields.RichTextField(
                        blank=True,
                        help_text="не более 5000 символов",
                        max_length=5000,
                        null=True,
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("date_updated", models.DateTimeField(auto_now=True)),
                ("slug", models.SlugField()),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "likes_discussion",
                    models.ManyToManyField(
                        blank=True,
                        related_name="discussion_likes",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Лайки",
                    ),
                ),
                (
                    "saves_discussion",
                    models.ManyToManyField(
                        blank=True,
                        related_name="blog_discussion_save",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Сохранённые посты пользователя",
                    ),
                ),
            ],
            options={
                "verbose_name": "Дискуссия",
                "verbose_name_plural": "Дискуссии",
            },
        ),
    ]
