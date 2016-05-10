from django import forms

from .models import jobs

class PostForm(forms.ModelForm):

    class Meta:
        model = jobs
        fields = ('name','description','group')