# 綁定 html --> edit/show/edit/index

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Nanny


def index(request):
    nannies = Nanny.objects.all()
    return render(request, "nannies/index.html", {"nannies": nannies})
    # 綁定 index.html


def show(request, id):
    nanny = get_object_or_404(Nanny, pk=id)
    if request.method == "POST":
        nanny.name = request.POST["name"]
        nanny.gender = request.POST["gender"]
        nanny.tel = request.POST["tel"]
        nanny.nickname = request.POST["name"]
        nanny.description = request.POST["description"]
        nanny.save()

        return redirect(f"/nannies/{nanny.id}")
    else:
        return render(request, "nannies/show.html", {"nanny": nanny})  # 綁定 show.html


def new(request):
    return render(request, "nannies/new.html")  # 綁定 new.html


def edit(request):
    nanny = get_object_or_404(Nanny, pk=id)
    return render(request, "nannies/edit.html", {"nanny": nanny})  # 綁定 edit.html


@require_POST
def create(request):
    nanny = Nanny(
        name=request.POST["name"],
        gender=request.POST["gender"],
        tel=request.POST["tel"],
        nickname=request.POST["name"],
        description=request.POST["description"],
    )
    nanny.save()
    return redirect("nannies:index")


@require_POST
def delete(request, id):
    nanny = get_object_or_404(Nanny, pk=id)
    nanny.delete()
    return redirect("nannies:index")
