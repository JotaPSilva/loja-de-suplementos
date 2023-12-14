from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto, Categoria
from .forms import AdicionarProdutoForm, AdicionarCategoriaForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from carrinho.models import Carrinho
from django.contrib.auth.decorators import user_passes_test


def index(request):
    pesquisa = request.GET.get("q")

    if pesquisa:
        produtos = Produto.objects.filter(nome__icontains=pesquisa)
    else:
        produtos = Produto.objects.all()

    paginator = Paginator(produtos, 6)
    numero_pagina = request.GET.get("page", 1)
    produtos_por_pagina = paginator.get_page(numero_pagina)

    categorias = Categoria.objects.all()
    context = {
        "produtos": produtos_por_pagina,
        "total_de_produtos": len(produtos),
        "categorias": categorias,
    }
    return render(request, "index.html", context)


def detalhar_produto(request, produto_id):
    if request.method == "POST":
        produto = Produto.objects.get(pk=produto_id)

        produto_do_carrinho, criado = Carrinho.objects.get_or_create(
            produto=produto, usuario=request.user
        )

        quantidade = int(request.POST.get("quantidade"))

        if not criado:
            # Se o produto já existir no carrinho, apenas atualiza a quantidade
            produto_do_carrinho.quantidade += quantidade
        else:
            # Se o produto não existir no carrinho, cria um novo item
            produto_do_carrinho.quantidade = quantidade

        produto_do_carrinho.save()
        return redirect("carrinho")

    produto = get_object_or_404(Produto, pk=produto_id)
    categorias = Categoria.objects.all()
    context = {"produto": produto, "categorias": categorias}
    return render(request, "detalhe_produto.html", context)


@login_required(login_url="/login/")
@user_passes_test(lambda u: u.is_superuser)
def adicionar_produto(request):
    if request.method == "POST":
        form = AdicionarProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = AdicionarProdutoForm()

    context = {"form": form}
    return render(request, "adicionar_produto.html", context)


@login_required(login_url="/login/")
@user_passes_test(lambda u: u.is_superuser)
def adicionar_categoria(request):
    if request.method == "POST":
        form = AdicionarCategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = AdicionarCategoriaForm()

    context = {"form": form}
    return render(request, "adicionar_categoria.html", context)


def produto_por_categoria(request, id):
    categorias = Categoria.objects.all()
    produtos = Produto.objects.filter(categoria=id)
    return render(
        request,
        "index.html",
        {
            "produtos": produtos,
            "categorias": categorias,
            "total_de_produtos": len(produtos),
        },
    )


@login_required(login_url="/login/")
@user_passes_test(lambda u: u.is_superuser)
def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    if request.method == "POST":
        form = AdicionarProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = AdicionarProdutoForm(instance=produto)

    context = {"form": form}
    return render(request, "editar_produto.html", context)


@login_required(login_url="/login/")
@user_passes_test(lambda u: u.is_superuser)
def excluir_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    produto.delete()
    return redirect("index")


@login_required(login_url="/login/")
@user_passes_test(lambda u: u.is_superuser)
def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, pk=id)
    if request.method == "POST":
        form = AdicionarCategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = AdicionarCategoriaForm(instance=categoria)

    context = {"form": form, "categoria": categoria}
    return render(request, "editar_categoria.html", context)


@login_required(login_url="/login/")
@user_passes_test(lambda u: u.is_superuser)
def excluir_categoria(request, id):
    categoria = get_object_or_404(Categoria, pk=id)
    categoria.delete()
    return redirect("index")
