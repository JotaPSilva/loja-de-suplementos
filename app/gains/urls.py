from .views import (
    index,
    detalhar_produto,
    adicionar_produto,
    adicionar_categoria,
    produto_por_categoria,
    editar_produto,
    excluir_produto,
)
from django.urls import path

urlpatterns = [
    path("", index, name="index"),
    path("<int:produto_id>/", detalhar_produto, name="detalhar_produto"),
    path("adicionar_produto/", adicionar_produto, name="adicionar_produto"),
    path("adicionar_categoria/", adicionar_categoria, name="adicionar_categoria"),
    path(
        "categoria/<int:id>/",
        produto_por_categoria,
        name="produto_por_categoria",
    ),
    path("editar_produto/<int:produto_id>/", editar_produto, name="editar_produto"),
    path("excluir_produto/<int:produto_id>/", excluir_produto, name="excluir_produto"),
]
