from django import forms
from django.forms import ModelForm
from ckeditor_uploader.fields import RichTextUploadingField
from blog.models import *


# class Form_Post(forms.Form):
#     titulo = forms.CharField(max_length=255)
#     intro = forms.CharField(max_length=255)
#     imagen = forms.ImageField(label="Imagen")
#     contenido = RichTextUploadingField() # CKEditor Rich Text Field

class Form_Post(ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'intro', 'contenido', 'imagen']