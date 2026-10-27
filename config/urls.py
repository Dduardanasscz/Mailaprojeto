
from django.contrib import admin
from django.urls import path
from django.shortcuts import render

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: render(request, 'cadastrar.html'), name='cadastrar'),
    path('login/', lambda request: render(request, 'login.html'), name='login'),
    path('index/', lambda request: render(request, 'index.html'), name='index'),
    path('mapa/', lambda request: render(request, 'mapa.html'), name='mapa'),
    path('mensagens/', lambda request: render(request, 'mensagens.html'), name='mensagens'),
    path('objetos/', lambda request: render(request, 'objetos.html'), name='objetos'),
    path('registrar/', lambda request: render(request, 'registrar.html'), name='registrar'),
    path('configuracoes/', lambda request: render(request, 'configuracoes.html'), name='configuracoes'),
    path('base/', lambda request: render(request, 'base.html'), name='configuracoes'),
]

