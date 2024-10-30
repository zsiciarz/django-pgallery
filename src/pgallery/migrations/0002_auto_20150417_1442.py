from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ("pgallery", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="tags",
            field=django.contrib.postgres.fields.ArrayField(
                default=[],
                size=None,
                base_field=models.CharField(max_length=64),
                blank=True,
            ),
        ),
    ]
