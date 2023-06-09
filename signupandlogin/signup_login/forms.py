from django import forms
from captcha.fields import CaptchaField

class Myform(forms.Form):
    captcha = CaptchaField()