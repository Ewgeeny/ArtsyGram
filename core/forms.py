from django import forms

from .models import Category


class CategoryFilterForm(forms.Form):
    tags = forms.CharField(
        required=False,
        label="Tag",
        widget=forms.TextInput(
            attrs={
                "onkeydown": "if(event.key===' '){event.preventDefault()}"
            }
        ),
    )

    def clean_tags(self):
        value = self.cleaned_data.get("tags", "")
        if " " in value:
            raise forms.ValidationError("Enter only one tag without spaces.")
        return value.strip().lstrip("#").lower()


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

    tags = forms.CharField(
        label="Tags",
        required=False,
        help_text="Separate tags with spaces",
    )


class EditPostForm(forms.Form):
    title = forms.CharField(
        label="Title",
        max_length=150,
    )

    description = forms.CharField(
        label="Description",
        widget=forms.Textarea,
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label="Category",
    )

    tags = forms.CharField(
        label="Tags",
        required=False,
        help_text="Separate tags with spaces",
    )