from django import forms


class IletisimForm(forms.Form):
    name = forms.CharField(max_length=50, label="Name", required=False)
    last_name = forms.CharField(max_length=50, label="Surname",required=False)
    email = forms.EmailField(max_length=50,label="Email",required=False)
    content = forms.CharField(max_length=1000, label="Content", required=False)
