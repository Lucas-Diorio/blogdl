from django import forms
# registros
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from usuarios.models import *

#  creacion del formulario
class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="ingrese Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)
    # clase anidada que configura el usercreation
    class Meta:
        model = User 
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields} #para cada uno de los campos de los formularios le asigna un valor vacio.


#  edición de usuario

# edituser

class UserEditForm(UserCreationForm):
    email=forms.EmailField()
    password1=forms.CharField(label="Ingrese contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repita contraseña", widget=forms.PasswordInput)
    first_name=forms.CharField(label="Modificar Nombre")
    last_name=forms.CharField(label="Modificar Apellido")

    # clase anidada que configura el usercreation
    class Meta:
        model = User 
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields} #para cada uno de los campos de los formularios le asigna un valor vacio.

class Form_Perfil(ModelForm):
    class Meta:
        model = Perfil
        fields = ['descripcion', 'avatar']