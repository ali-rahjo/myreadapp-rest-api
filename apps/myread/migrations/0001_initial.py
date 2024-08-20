# Generated by Django 5.1 on 2024-08-20 10:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("book", "0003_book_bookauthor_book_authors"),
        ("reader", "0002_reader"),
    ]

    operations = [
        migrations.CreateModel(
            name="MyRead",
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
                    "percentage_read",
                    models.PositiveSmallIntegerField(blank=True, null=True),
                ),
                ("start_read_date", models.DateField(blank=True, null=True)),
                ("end_read_date", models.DateField(blank=True, null=True)),
                (
                    "book_isbn",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="book.book"
                    ),
                ),
                (
                    "reader_username",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="reader.reader"
                    ),
                ),
            ],
            options={
                "constraints": [
                    models.CheckConstraint(
                        condition=models.Q(
                            ("percentage_read__gte", 0), ("percentage_read__lte", 100)
                        ),
                        name="myread_myread_per_read_check",
                    ),
                    models.CheckConstraint(
                        condition=models.Q(
                            ("end_read_date__gt", models.F("start_read_date"))
                        ),
                        name="myread_myread_end_read_start_read_date_check",
                    ),
                    models.CheckConstraint(
                        condition=models.Q(
                            models.Q(
                                ("percentage_read__exact", 0),
                                ("start_read_date__isnull", True),
                            ),
                            models.Q(
                                ("percentage_read__gt", 0),
                                ("start_read_date__isnull", False),
                            ),
                            _connector="OR",
                        ),
                        name="myread_myread_per_read_start_read_date_check",
                    ),
                    models.CheckConstraint(
                        condition=models.Q(
                            models.Q(
                                ("end_read_date__isnull", False),
                                ("percentage_read__exact", 100),
                            ),
                            models.Q(
                                ("end_read_date__isnull", True),
                                ("percentage_read__lt", 100),
                            ),
                            _connector="OR",
                        ),
                        name="myread_myread_per_read_end_read_date_check",
                    ),
                ],
                "unique_together": {
                    ("book_isbn", "reader_username", "start_read_date")
                },
            },
        ),
    ]
