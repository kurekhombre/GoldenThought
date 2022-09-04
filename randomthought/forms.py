from django import forms
from randomthought.models import RandomThought


class RandomThoughtFormDjango(forms.Form):
    thought = forms.CharField(widget=forms.Textarea, label="Thought")
    author = forms.CharField(label="Author")


class RandomThoughtForm(forms.ModelForm):
    class Meta:
        model = RandomThought
        fields = '__all__'
        labels = {
            "thought": "Thought",
            "author": "Author",
        }
