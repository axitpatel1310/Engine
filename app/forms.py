from django import forms
from .models import user

class loginform(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control'
            }
        )
    )
    

class Payment_details(forms.Form):
    class Meta:
        model = user
        fields = ("payment_method","payment_info")
        
        username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
                }
            )
        )
        password = forms.CharField(
            widget=forms.PasswordInput(
                attrs={
                    'class':'form-control'
                }
            )
        )