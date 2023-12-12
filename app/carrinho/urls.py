from .views import carrinho, remover_item_carrinho
from django.urls import path

urlpatterns = [
    path("carrinho", carrinho, name="carrinho"),
    path(
        "remover_item_carrinho/<int:id>/",
        remover_item_carrinho,
        name="remover_item_carrinho",
    ),
]
