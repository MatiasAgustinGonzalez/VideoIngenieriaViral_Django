from django.urls import path
from .views import(
    home_view,
    TarjetaInicioCreateView,
)

urlpatterns = [
    path("", home_view, name="WebSite_home"),
    path("cards-index/create/", TarjetaInicioCreateView.as_view(), name="create_cards-index"),

]