from django.db import migrations


def deduplicate_categories(apps, schema_editor):
    Category = apps.get_model("core", "Category")
    seen_names = set()
    for category in Category.objects.order_by("id"):
        if category.name in seen_names:
            category.delete()
        else:
            seen_names.add(category.name)


def reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0005_favorite"),
    ]
    operations = [
        migrations.RunPython(deduplicate_categories, reverse),
    ]
