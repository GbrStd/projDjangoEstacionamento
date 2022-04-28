from django.contrib import admin

# Register your models here.
from estacionamento.models import *

admin.site.register(Carro)
admin.site.register(Cliente)
admin.site.register(Vendedor)
admin.site.register(Fornecedor)
admin.site.register(Seguranca)
admin.site.register(Vaga)
