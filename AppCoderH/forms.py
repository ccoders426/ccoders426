from django import forms

class Curso_formulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()


class Profesor_formulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    dni = forms.IntegerField()
    celular = forms.CharField(max_length=15)
    email = forms.EmailField()
    curso = forms.CharField(max_length=40)


class Alumno_formulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    dni = forms.IntegerField()
    celular = forms.CharField(max_length=15)
    email = forms.EmailField()
    curso = forms.CharField(max_length=40)
    camada = forms.IntegerField()