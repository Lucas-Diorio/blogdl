from django import forms
# registros
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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