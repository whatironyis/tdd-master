from django.db import models

class jobs(models.Model):

    name = models.CharField(max_length=100, unique=True, verbose_name='Tytul')
    description = models.TextField(verbose_name="Opis")
    created = models.DateTimeField("Data dodania")
    finished = models.DateTimeField("Termin zakonczenia")
    assign = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class wip(models.Model):

    name = models.CharField(max_length=100, unique=True, verbose_name='Tytul')
    description = models.TextField(verbose_name="Opis")
    created = models.DateTimeField("Data dodania")
    finished = models.DateTimeField("Termin zakonczenia")
    assign = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class donejob(models.Model):

    name = models.CharField(max_length=100, unique=True, verbose_name='Tytul')
    description = models.TextField(verbose_name="Opis")
    created = models.DateTimeField("Data dodania")
    finished = models.DateTimeField("Termin zakonczenia")
    assign = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name