# Generated by Django 5.1 on 2024-08-13 15:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="video_url",
            field=models.URLField(
                blank=True, null=True, verbose_name="Ссылка на видео"
            ),
        ),
        migrations.CreateModel(
            name="Payment",
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
                ("payment_date", models.DateField(verbose_name="Дата оплаты")),
                (
                    "payment_amount",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Сумма оплаты"
                    ),
                ),
                (
                    "payment_method",
                    models.CharField(
                        choices=[("cash", "Наличные"), ("transfer", "Перевод на счет")],
                        max_length=20,
                        verbose_name="Способ оплаты",
                    ),
                ),
                (
                    "paid_course",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="courses.course",
                        verbose_name="Оплаченный курс",
                    ),
                ),
                (
                    "separately_paid_lesson",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="courses.lesson",
                        verbose_name="Отдельно оплаченный урок",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="payments",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Платеж",
                "verbose_name_plural": "Платежи",
            },
        ),
    ]
