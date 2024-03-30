from django.shortcuts import render, redirect
from AppCoderH.models import *
from django.http import HttpResponse
from django.template import loader
from AppCoderH.forms import *
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,"home.html")

# --- Cursos ---

def ver_cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos": cursos}
    cursos_alta = loader.get_template("ver_cursos.html")
    documento = cursos_alta.render(dicc)
    return HttpResponse(documento)

def formulario_cursos(request):
    if request.method == "POST":
        
        mi_formulario_cur = Curso_formulario(request.POST)

        if mi_formulario_cur.is_valid():
            datos = mi_formulario_cur.cleaned_data
            curso = Curso(nombre=datos["nombre"], camada=datos["camada"])
            curso.save()
            return render(request, "formulario_cursos.html")
        
    return render(request, "formulario_cursos.html")

def buscar_curso(request):
    
    return render(request, "buscar_curso.html")

def buscar_curs(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains=nombre)
        return render(request,"result_busqueda_cursos.html", {"cursos":cursos})
    else:
        return HttpResponse("Ingrese el nombre del curso")
    
def elimina_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    messages.success(request, "eliminado correctamente")

    curso = Curso.objects.all()
    return render(request, "ver_cursos.html", {"cursos":curso})

def edita_curso(request, id):
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
            return render(request, "ver_cursos.html", {"cursos":curso})

    else:
        mi_formulario_cur = Curso_formulario(initial={"nombre":curso.nombre, "camada":curso.camada})
    
    return render(request, "edita_curso.html", {"mi_formulario_cur":mi_formulario_cur, "curso":curso})


# --- Profesores ---

def ver_profesores(request):
    profesores = Profesor.objects.all()
    dicc = {"profesores": profesores}
    profesores_alta = loader.get_template("ver_profesores.html")
    documento = profesores_alta.render(dicc)
    return HttpResponse(documento)

def formulario_profesores(request):
    if request.method == "POST":
        
        mi_formulario_profe = Profesor_formulario(request.POST)

        if mi_formulario_profe.is_valid():
            datos = mi_formulario_profe.cleaned_data
            profesor = Profesor(nombre=datos["nombre"], apellido=datos["apellido"], dni=datos["dni"], celular=datos["celular"], email=datos["email"], curso=datos["curso"])
            profesor.save()
            return render(request, "formulario_profesores.html")
        
    return render(request, "formulario_profesores.html")

def buscar_profesor(request):
    
    return render(request, "buscar_profesor.html")

def buscar_profe(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        profesores = Profesor.objects.filter(nombre__icontains=nombre)
        return render(request,"result_busqueda_profesores.html", {"profesores":profesores})
    else:
        return HttpResponse("Ingrese el nombre del profesor")
    
def elimina_profesor(request, id):
    profesor = Profesor.objects.get(id=id)
    profesor.delete()
    messages.success(request, "eliminado correctamente")

    profesor = Profesor.objects.all()
    return render(request, "ver_profesores.html", {"profesores":profesor})

def edita_profesor(request, id):
    profesor = Profesor.objects.get(id=id)

    if request.method == "POST":
        
        mi_formulario_profe = Profesor_formulario(request.POST)
        if mi_formulario_profe.is_valid():
            datos = mi_formulario_profe.cleaned_data
            profesor.nombre = datos["nombre"]
            profesor.apellido = datos["apellido"]
            profesor.dni = datos["dni"]
            profesor.celular = datos["celular"]
            profesor.email = datos["email"]
            profesor.curso = datos["curso"]
            profesor.save()
            messages.success(request, "modificado correctamente")

            profesor = Profesor.objects.all()
            return render(request, "ver_profesores.html", {"profesores":profesor})

    else:
        mi_formulario_profe = Profesor_formulario(initial={"nombre":profesor.nombre, "apellido":profesor.apellido, "dni":profesor.dni, "celular":profesor.celular, "email":profesor.email, "curso":profesor.curso})
    
    return render(request, "edita_profesor.html", {"mi_formulario_profe":mi_formulario_profe, "profesor":profesor})


# --- Alumnos ---

def ver_alumnos(request):
    alumnos = Alumno.objects.all()
    dicc = {"alumnos": alumnos}
    alumnos_alta = loader.get_template("ver_alumnos.html")
    documento = alumnos_alta.render(dicc)
    return HttpResponse(documento)

def formulario_alumnos(request):
    if request.method == "POST":
        
        mi_formulario_alumn = Alumno_formulario(request.POST)

        if mi_formulario_alumn.is_valid():
            datos = mi_formulario_alumn.cleaned_data
            alumno = Alumno(nombre=datos["nombre"], apellido=datos["apellido"], dni=datos["dni"], celular=datos["celular"], email=datos["email"], curso=datos["curso"], camada=datos["camada"])
            alumno.save()
            return render(request, "formulario_alumnos.html")
        
    return render(request, "formulario_alumnos.html")

def buscar_alumno(request):
    
    return render(request, "buscar_alumno.html")

def buscar_alum(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        alumnos = Alumno.objects.filter(nombre__icontains=nombre)
        return render(request,"result_busqueda_alumnos.html", {"alumnos":alumnos})
    else:
        return HttpResponse("Ingrese el nombre del alumno")
    
def elimina_alumno(request, id):
    alumno = Alumno.objects.get(id=id)
    alumno.delete()
    messages.success(request, "eliminado correctamente")

    alumno = Alumno.objects.all()
    return render(request, "ver_alumnos.html", {"alumnos":alumno})

def edita_alumno(request, id):
    alumno = Alumno.objects.get(id=id)

    if request.method == "POST":
        
        mi_formulario_alumn = Alumno_formulario(request.POST)
        if mi_formulario_alumn.is_valid():
            datos = mi_formulario_alumn.cleaned_data
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
            return render(request, "ver_alumnos.html", {"alumnos":alumno})

    else:
        mi_formulario_alumn = Alumno_formulario(initial={"nombre":alumno.nombre, "apellido":alumno.apellido, "dni":alumno.dni, "celular":alumno.celular, "email":alumno.email, "curso":alumno.curso, "camada":alumno.camada})
    
    return render(request, "edita_alumno.html", {"mi_formulario_alumn":mi_formulario_alumn, "alumno":alumno})