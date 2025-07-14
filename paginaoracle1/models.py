from django.db import models

# Create your models here.
class tecnologia_apoyo(models.Model):
    tecnologia_progra = models.CharField(max_length=100)
    relacion_desc = models.TextField()

    def __str__(self):
        return self.tecnologia_progra