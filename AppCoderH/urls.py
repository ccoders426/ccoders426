from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [

    path("", views.home, name="home"),

    # --- cursos --- 

    path("formulario_cursos", views.formulario_cursos),
    path("ver_cursos", views.ver_cursos, name="cursos"),
    path("buscar_curso", views.buscar_curso),
    path("buscar_curs", views.buscar_curs),
    path("elimina_curso/<int:id>", views.elimina_curso, name="elimina_curso"),
    path("edita_curso/<int:id>", views.edita_curso, name="edita_curso"),


    # --- profesores ---

    path("formulario_profesores", views.formulario_profesores),
    path("ver_profesores", views.ver_profesores, name="profesores"),
    path("buscar_profesor", views.buscar_profesor),
    path("buscar_profe", views.buscar_profe),
    path("elimina_profesor/<int:id>", views.elimina_profesor, name="elimina_profesor"),
    path("edita_profesor/<int:id>", views.edita_profesor, name="edita_profesor"),


    # --- alumnos ---

    path("formulario_alumnos", views.formulario_alumnos),
    path("ver_alumnos", views.ver_alumnos, name="alumnos"),
    path("buscar_alumno", views.buscar_alumno),
    path("buscar_alum", views.buscar_alum),
    path("elimina_alumno/<int:id>", views.elimina_alumno, name="elimina_alumno"),
    path("edita_alumno/<int:id>", views.edita_alumno, name="edita_alumno"),

    
    # --- login ---
    
    path("login", views.login_request, name="Login"),

    
    # --- Registro ---
    
    path("register", views.register, name="Register"),

    # --- Logout ---

    path("logout", LogoutView.as_view(template_name="logout.html"), name="Logout"),

    # --- Editar perfil ---

    path("editarPerfil", views.editarPerfil, name="EditarPerfil"),

    # --- Account ---

    path("account", views.account, name="account")

    

]