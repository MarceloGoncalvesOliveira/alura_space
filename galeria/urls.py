from django.urls import path
from galeria.views import index, imagem, buscar

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>/', imagem, name='imagem'),  # Adicione a barra final e uma vírgula
    path('buscar/', buscar, name='buscar')  # Corrigi 'nome' para 'name' e adicionei a barra final
]
