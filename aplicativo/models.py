from django.db import models

# Create your models here.
class Lista(models.Model):
    name = models.CharField(max_length=25)
    desc = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.id}, {self.name}"


class Item(models.Model):
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE)
    texto = models.CharField(max_length=40)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}, {self.texto}, {self.status}, {self.lista}"