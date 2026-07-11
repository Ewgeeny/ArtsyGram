from django import forms

from .models import Category


class CategoryFilterForm(forms.Form):
    category = forms.ChoiceField(
        label="Category",
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        choices = [("", "All categories")]

        for category in Category.objects.all():
            choices.append((str(category.id), category.name))

        self.fields["category"].choices = choices