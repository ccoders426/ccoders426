from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Curso_formulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()


class Profesor_formulario(forms.Form):

    avatar = forms.ImageField()
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    dni = forms.IntegerField()
    celular = forms.CharField(max_length=15)
    email = forms.EmailField()
    curso = forms.CharField(max_length=40)


class Alumno_formulario(forms.Form):
    avatar = forms.ImageField()
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    dni = forms.IntegerField()
    celular = forms.CharField(max_length=15)
    email = forms.EmailField()
    curso = forms.CharField(max_length=40)
    camada = forms.IntegerField()

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Nueva contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_text = {k:"" for k in fields}