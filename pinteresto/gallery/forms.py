from user.models import *
from django import forms


class AddPostForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'photo', 'category', 'teg']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            # 'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'teg': forms.Select(attrs={'class': 'form-control'}),
        }


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']
        widgets = {'comments': forms.TextInput(attrs={'class': 'form-control'})}


class SearchForm(forms.Form):
    query = forms.CharField()
