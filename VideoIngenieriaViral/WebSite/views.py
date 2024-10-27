from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import TarjetaInicio


def home_view(request):
    return render(request, "WebSite/pages/index.html")


# -----------------------------------------------------------------------------
# --------------------------------   CRUD   -----------------------------------
# -----------------------------------------------------------------------------


#--------------------------------
#   LISTAR todos los registros
#--------------------------------





#--------------------------------
#   CREAR todos los registros
#--------------------------------





#--------------------------------
#   LEER todos los registros
#--------------------------------





#--------------------------------
# ACTUALIZAR todos los registros
#--------------------------------





#--------------------------------
#   BORRAR todos los registros
#--------------------------------







# -----------------------------------------------------------------------------
# ----------------------------   PERFILES   -----------------------------------
# -----------------------------------------------------------------------------