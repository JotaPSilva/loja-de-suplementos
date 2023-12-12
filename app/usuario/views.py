from .forms import RegistrarForm
from django.shortcuts import redirect, render


def registrar(request):
    if request.method == "POST":
        form = RegistrarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegistrarForm()
    return render(request, "registrar.html", {"form": form})
