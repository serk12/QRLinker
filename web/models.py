from django.db import models

class Sesion(models.Model):
    token = models.CharField(max_length=200, verbose_name='Token', null=False, primary_key=True)

    def __str__(self):
        return self.token

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/')
    token = models.CharField(max_length=200, verbose_name='Token', null=False)
    def __str__(self):
        return self.docfile.name

