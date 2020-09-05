from django.db import models

class Enquete(models.Model):
    texto = models.CharField(max_length=100)
    data_publicacao = models.DateField()
    
    