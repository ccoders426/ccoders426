from django.shortcuts import render, redirect
from AppCoderH.models import *
from django.http import HttpResponse
from django.template import loader
from AppCoderH.forms import *
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


# Create your views here.

def home(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request,"home.html", {"url":avatares[0].imagen.url if avatares.exists () else None})

# --- Login ---

def login_request(request):    

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contra)
            

            if user is not None:                
                login(request, user)
                avatares = Avatar.objects.filter(user=request.user.id)                
                return render(request, "inicio.html", {"url":avatares[0].imagen.url, "mensaje":f"Bienvenido/a {usuario}", "usuario":usuario})
                #return render(request, "inicio.html", {"mensaje":f"Bienvenido/a {usuario}", "usuario":usuario})
            else:
                return HttpResponse(f"usuaruio no encontrado")            
        else:
            return HttpResponse(f"FORM INCORRECTO {form}")

    form = AuthenticationForm()
    return render(request, "login.html", {"form":form})


# --- Registro ---

def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Usuario creado")        
    
    else:
        form = UserCreationForm()
    return render(request, "registro.html", {"form":form})


# --- Editar Perfil ---

def editarPerfil(request):

    usuario = request.user
    if request.method == "POST":        
        usuario = request.user
        if request.method == "POST":
            mi_formulario = UserEditForm(request.POST)
            if mi_formulario.is_valid():
                informacion = mi_formulario.cleaned_data
                usuario.email = informacion["email"]
                password = informacion["password1"]
                usuario.set_password(password)
                usuario.save()
                return render(request, "inicio.html")
    
    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})
    
    return render(request, "editar_perfil.html", {"miFormulario":miFormulario, "usuario":usuario})


# --- Cursos ---


def ver_cursos(request):
    cursos = Curso.objects.all()
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request , "ver_cursos.html", {"cursos": cursos,"url":avatares[0].imagen.url if avatares.exists () else None})

@login_required
def formulario_cursos(request):

    avatares = Avatar.objects.filter(user=request.user.id)

    if request.method == "POST":
        
        mi_formulario_cur = Curso_formulario(request.POST)

        if mi_formulario_cur.is_valid():
            datos = mi_formulario_cur.cleaned_data
            curso = Curso(nombre=datos["nombre"], camada=datos["camada"])
            curso.save()
            return render(request, "formulario_cursos.html", {"url":avatares[0].imagen.url if avatares.exists () else None})
        
    return render(request, "formulario_cursos.html", {"url":avatares[0].imagen.url if avatares.exists () else None})


def buscar_curso(request):

    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, "buscar_curso.html", {"url":avatares[0].imagen.url if avatares.exists () else None})
    

def buscar_curs(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains=nombre)
        return render(request,"result_busqueda_cursos.html", {"cursos":cursos, "url":avatares[0].imagen.url if avatares.exists () else None})
    else:
        return HttpResponse("Ingrese el nombre del curso")


@login_required    
def elimina_curso(request, id):
    avatares = Avatar.objects.filter(user=request.user.id)
    curso = Curso.objects.get(id=id)
    curso.delete()
    messages.success(request, "eliminado correctamente", {"url":avatares[0].imagen.url if avatares.exists () else None})

    curso = Curso.objects.all()
    return render(request, "ver_cursos.html", {"cursos":curso, "url":avatares[0].imagen.url if avatares.exists () else None})


def edita_curso(request, id):
    avatares = Avatar.objects.filter(user=request.user.id)
    curso = Curso.objects.get(id=id)

    if request.method == "POST":
        
        mi_formulario_cur = Curso_formulario(request.POST)
        if mi_formulario_cur.is_valid():
            datos = mi_formulario_cur.cleaned_data
            curso.nombre = datos["nombre"]
            curso.camada = datos["camada"]
            curso.save()
            messages.success(request, "modificado correctamente")

            curso = Curso.objects.all()
            return render(request, "ver_cursos.html", {"cursos":curso, "url":avatares[0].imagen.url if avatares.exists () else None})

    else:
        mi_formulario_cur = Curso_formulario(initial={"nombre":curso.nombre, "camada":curso.camada})
    
    return render(request, "edita_curso.html", {"mi_formulario_cur":mi_formulario_cur, "curso":curso, "url":avatares[0].imagen.url if avatares.exists () else None})


# --- Profesores ---


def ver_profesores(request):
    profesores = Profesor.objects.all()
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request , "ver_profesores.html", {"profesores": profesores, "url":avatares[0].imagen.url if avatares.exists () else None})
    

@login_required

def formulario_profesores(request):
    avatares = Avatar.objects.filter(user=request.user.id)

    if request.method == "POST":
        
        mi_formulario_profe = Profesor_formulario(request.POST)

        if mi_formulario_profe.is_valid():
            datos = mi_formulario_profe.cleaned_data
            profesor = Profesor(nombre=datos["nombre"], apellido=datos["apellido"], dni=datos["dni"], celular=datos["celular"], email=datos["email"], curso=datos["curso"])
            profesor.save()
            return render(request, "formulario_profesores.html", {"url":avatares[0].imagen.url if avatares.exists () else None})
        
    return render(request, "formulario_profesores.html", {"url":avatares[0].imagen.url if avatares.exists () else None})

def buscar_profesor(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, "buscar_profesor.html", {"url":avatares[0].imagen.url if avatares.exists () else None})

def buscar_profe(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        profesores = Profesor.objects.filter(nombre__icontains=nombre)
        return render(request,"result_busqueda_profesores.html", {"profesores":profesores, "url":avatares[0].imagen.url if avatares.exists () else None})
    else:
        return HttpResponse("Ingrese el nombre del profesor")

@login_required    
def elimina_profesor(request, id):
    avatares = Avatar.objects.filter(user=request.user.id)
    profesor = Profesor.objects.get(id=id)
    profesor.delete()
    messages.success(request, "eliminado correctamente")

    profesor = Profesor.objects.all()
    return render(request, "ver_profesores.html", {"profesores":profesor, "url":avatares[0].imagen.url if avatares.exists () else None})

@login_required
def edita_profesor(request, id):
    avatares = Avatar.objects.filter(user=request.user.id)
    profesor = Profesor.objects.get(id=id)

    if request.method == "POST":
        
        mi_formulario_profe = Profesor_formulario(request.POST)
        if mi_formulario_profe.is_valid():
            datos = mi_formulario_profe.cleaned_data
            profesor.avatar = datos["avatar"]
            profesor.nombre = datos["nombre"]
            profesor.apellido = datos["apellido"]
            profesor.dni = datos["dni"]
            profesor.celular = datos["celular"]
            profesor.email = datos["email"]
            profesor.curso = datos["curso"]
            profesor.save()
            messages.success(request, "modificado correctamente")

            profesor = Profesor.objects.all()
            return render(request, "ver_profesores.html", {"profesores":profesor, "url":avatares[0].imagen.url if avatares.exists () else None})

    else:
        mi_formulario_profe = Profesor_formulario(initial={"nombre":profesor.nombre, "apellido":profesor.apellido, "dni":profesor.dni, "celular":profesor.celular, "email":profesor.email, "curso":profesor.curso})
    
    return render(request, "edita_profesor.html", {"mi_formulario_profe":mi_formulario_profe, "profesor":profesor, "url":avatares[0].imagen.url if avatares.exists () else None})


# --- Alumnos ---

@login_required
def ver_alumnos(request):
    alumnos = Alumno.objects.all()
    avatares = Avatar.objects.filter(user=request.user.id)    
    return render(request , "ver_alumnos.html", {"alumnos": alumnos, "url":avatares[0].imagen.url if avatares.exists () else None})


@login_required
def formulario_alumnos(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if request.method == "POST":
        
        mi_formulario_alumn = Alumno_formulario(request.POST)

        if mi_formulario_alumn.is_valid():
            datos = mi_formulario_alumn.cleaned_data
            alumno = Alumno(nombre=datos["nombre"], apellido=datos["apellido"], dni=datos["dni"], celular=datos["celular"], email=datos["email"], curso=datos["curso"], camada=datos["camada"])
            alumno.save()
            return render(request, "formulario_alumnos.html", {"url":avatares[0].imagen.url if avatares.exists () else None})
        
    return render(request, "formulario_alumnos.html", {"url":avatares[0].imagen.url if avatares.exists () else None})

@login_required
def buscar_alumno(request):
    avatares = Avatar.objects.filter(user=request.user.id)    
    return render(request, "buscar_alumno.html", {"url":avatares[0].imagen.url if avatares.exists () else None})

@login_required
def buscar_alum(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        alumnos = Alumno.objects.filter(nombre__icontains=nombre)
        return render(request,"result_busqueda_alumnos.html", {"alumnos":alumnos, "url":avatares[0].imagen.url if avatares.exists () else None})
    else:
        return HttpResponse("Ingrese el nombre del alumno")

@login_required    
def elimina_alumno(request, id):
    avatares = Avatar.objects.filter(user=request.user.id)
    alumno = Alumno.objects.get(id=id)
    alumno.delete()
    messages.success(request, "eliminado correctamente")

    alumno = Alumno.objects.all()
    return render(request, "ver_alumnos.html", {"alumnos":alumno, "url":avatares[0].imagen.url if avatares.exists () else None})

@login_required
def edita_alumno(request, id):
    avatares = Avatar.objects.filter(user=request.user.id)
    alumno = Alumno.objects.get(id=id)

    if request.method == "POST":
        
        mi_formulario_alumn = Alumno_formulario(request.POST)
        if mi_formulario_alumn.is_valid():
            datos = mi_formulario_alumn.cleaned_data
            alumno.avatar = datos["avatar"]
            alumno.nombre = datos["nombre"]
            alumno.apellido = datos["apellido"]
            alumno.dni = datos["dni"]
            alumno.celular = datos["celular"]
            alumno.email = datos["email"]
            alumno.curso = datos["curso"]
            alumno.camada = datos["camada"]
            alumno.save()
            messages.success(request, "modificado correctamente")

            alumno = Alumno.objects.all()
            return render(request, "ver_alumnos.html", {"alumnos":alumno, "url":avatares[0].imagen.url if avatares.exists () else None})

    else:
        mi_formulario_alumn = Alumno_formulario(initial={"nombre":alumno.nombre, "apellido":alumno.apellido, "dni":alumno.dni, "celular":alumno.celular, "email":alumno.email, "curso":alumno.curso, "camada":alumno.camada})
    
    return render(request, "edita_alumno.html", {"mi_formulario_alumn":mi_formulario_alumn, "alumno":alumno, "url":avatares[0].imagen.url if avatares.exists () else None})


# --- Account ---

@login_required
def account(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    usuario = request.user

    if request.method == "POST":
        
        usuario = request.user

        if request.method == "POST":

            mi_formulario = UserEditForm(request.POST)

            if mi_formulario.is_valid():

                informacion = mi_formulario.cleaned_data
                usuario.email = informacion["email"]
                password = informacion["password1"]
                usuario.set_password(password)
                usuario.save()
                return render(request, "account.html", {"url":avatares[0].imagen.url if avatares.exists () else None})
    
    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})
    
    return render(request, "account.html", {"miFormulario":miFormulario, "usuario":usuario, "url":avatares[0].imagen.url if avatares.exists () else None})