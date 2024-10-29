from galeria.models import Fotografia

# Veja todos os objetos no banco de dados
print(Fotografia.objects.all())

# Conte o número de objetos na tabela
print(Fotografia.objects.count())
