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
    path("mostrar/<id>/",views.mostrar,name="mostrar"),
    path("compras/<id>/",views.compras,name="compras"),
    path("listaCompra",views.listaCompra,name="listaCompra"),
    path("eliminar_compra/<id>/",views.eliminar_compra,name="eliminar_compra"),
    path("modificar_compra/<id>/",views.modificar_compra,name="modificar_compra")
]