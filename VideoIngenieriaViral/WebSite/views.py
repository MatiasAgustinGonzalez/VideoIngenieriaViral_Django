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

class TarjetaInicioCreateView(CreateView):
    model = TarjetaInicio
    template_name = "WebSite/forms/form_create_cards.html"
    fields = ['titulo', 'cuerpo']
    success_url = reverse_lazy("list_cards")



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