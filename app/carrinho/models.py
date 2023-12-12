from django.db import models
from django.contrib.auth.models import User
from gains.models import Produto


class Carrinho(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_total(self):
        return self.produto.preco * self.quantidade
