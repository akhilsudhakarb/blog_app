from django import forms
from .models import  Blogs

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ['category', 'title', 'author', 'content', 'image']

        widgets = {

            'title':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'authr', 'type': 'hidden'}),

            'category': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ['title', 'content']

        widgets = {

            'title':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

