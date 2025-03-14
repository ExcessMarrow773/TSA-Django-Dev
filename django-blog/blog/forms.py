# blog/forms.py

from django import forms
from .models import Category  # Import the Category model

class CommentForm(forms.Form):
    body = forms.CharField(
        max_length=255,
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Leave a comment!"}
        )
    )
class DeletePost(forms.Form):
    AreYouSure = forms.BooleanField(required=True)
class CreateCategory(forms.Form):
    name = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "New Category"})
        )
    
class CreatePost(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = False
    title = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Title"}
        ),
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Body"}
        )
    )
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={"class": "form-control"}
        )
    )
    image = forms.ImageField(
        widget=forms.FileInput(
            attrs={"class": "form-control", "required": "False"}
        )
    )

