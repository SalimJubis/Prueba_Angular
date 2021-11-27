from django.urls import path
from .views import UsuarioView

urlpatterns=[
    path('usuario/',UsuarioView.as_view(),name='usuario_list'),
    path('usuario/<mail>',UsuarioView.as_view(),name='usuario_process')
]