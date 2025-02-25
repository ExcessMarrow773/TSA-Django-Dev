# blog/forms.py

from django import forms
from .models import Category  # Import the Category model

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your Name"}
        ),
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Leave a comment!"}
        )
    )
class CreatePost(forms.Form):
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
            attrs={"class": "form-control", "type": "file"}
        )
    )