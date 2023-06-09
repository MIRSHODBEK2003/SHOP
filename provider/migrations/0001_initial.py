# Generated by Django 4.2.1 on 2023-05-11 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("product", "0002_alter_category_options_alter_product_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Income",
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
                    "income_id",
                    models.CharField(
                        default="#5eb849be-392a-467f-84ac-629ef63807fe",
                        max_length=255,
                        verbose_name="Mahsulot id raqami",
                    ),
                ),
                (
                    "total",
                    models.DecimalField(
                        decimal_places=2, max_digits=17, verbose_name="Summa"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Provider",
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
                    "name",
                    models.CharField(max_length=255, verbose_name="Yetkazib beruvchi"),
                ),
                (
                    "phone",
                    models.CharField(max_length=13, verbose_name="Telefon raqami"),
                ),
                (
                    "balance",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=17,
                        verbose_name="Yetkazib beruvchi Balansi",
                    ),
                ),
                (
                    "info",
                    models.TextField(verbose_name="Yetkazib beruvchi haqida ma'lumot"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="IncomeItem",
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
                ("count", models.SmallIntegerField(verbose_name="Soni")),
                (
                    "income",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="provider.income",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="product.product",
                        verbose_name="Mahsulot",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="income",
            name="provider",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="provider.provider",
                verbose_name="Yetkazib beruvchi",
            ),
        ),
    ]
