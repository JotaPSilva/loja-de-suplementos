from django.shortcuts import render, redirect, get_object_or_404
from .models import Carrinho
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login/")
def carrinho(request):
    produtos_carrinho = Carrinho.objects.filter(usuario=request.user)
    preco_total = sum(item.get_total() for item in produtos_carrinho)

    return render(
        request,
        "carrinho.html",
        {
            "carrinho": produtos_carrinho,
            "preco_total": preco_total,
        },
    )


def remover_item_carrinho(request, id):
    item = get_object_or_404(Carrinho, id=id)

    if item.quantidade > 1:
        item.quantidade -= 1
        item.save()
    else:
        item.delete()

    return redirect("carrinho")
