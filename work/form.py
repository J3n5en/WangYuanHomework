#coding:utf-8
__author__ = 'jensen'

from django import forms
class LoginForm(forms.Form):
    username = forms.CharField()
    phone = forms.CharField()
class FileForm(forms.Form):
    desc = forms.CharField()
    link = forms.FileField()
class newphoneform(forms.Form):
    newphone = forms.CharField()