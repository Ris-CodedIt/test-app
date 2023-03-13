from django.urls import  path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="mydrone/index.html")),
    path('drones/', views.register),
    path('available/', views.check_available),
    path('load/<did>/<mid>/', views.load_drone),
    path('check_med/<id>/', views.check_med),
    path('check_battery/<id>/', views.check_battery),
]