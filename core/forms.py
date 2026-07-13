from django import forms

from .models import Category


class CategoryFilterForm(forms.Form):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        empty_label="All categories",
        label="Category",
    )


class PostForm(forms.Form):
    title = forms.CharField(
        label="Title",
        max_length=150,
    )

    image = forms.ImageField(
        label="Image",
    )

    description = forms.CharField(
        label="Description",
        widget=forms.Textarea,
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label="Category",
    )