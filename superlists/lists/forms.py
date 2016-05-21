import re
from django.forms import *
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User, Group
from django.shortcuts import *
from django.template import RequestContext
from .models import jobs

class PostForm(ModelForm):
    class Meta:
        model = jobs
        fields = ('name','description')
        labels = { 'name': _(''),
                   'description': _('')}
        widgets = {
            'name': TextInput(attrs={'class': "form-control", "placeholder":"Name"}),
            'description': Textarea(attrs={'class': "form-control", "placeholder":"Description", 'rows': 5}),
        }
class RegistrationForm(Form):
    username = RegexField(regex=r'^\w+$', widget=TextInput(attrs={'class': "form-control","placeholder":"Nazwa uzytkownika"}),label=_(""), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    email = EmailField(widget=TextInput(attrs={'class': "form-control","placeholder":"E-Mail"}), label=_(""))
    password1 = CharField(widget=PasswordInput(attrs={'class': "form-control","placeholder":"Haslo"}), label=_(""))
    password2 = CharField(widget=PasswordInput(attrs={'class': "form-control","placeholder":"Ponownie haslo"}), label=_(""))

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data

class GroupForma(Form):
    groupy = CharField(widget=TextInput(attrs={'class': "form-control","placeholder":"Group"}), label=_(""))

