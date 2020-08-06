from django.urls import path
from . import views
urlpatterns=[
    path("register",views.register,name="register"),
    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout"),
    path("create_saucer",views.create_saucer,name="create_saucer"),
    path("listar",views.listar,name="listar"),
    path("create_cook",views.create_cook,name="create_cook"),
    path("eliminar/<id>/",views.eliminar,name="eliminar"),
    path("modificar/<id>/",views.modificar,name="modificar"),
    path("mostrar/<id>/",views.mostrar,name="mostrar")

]