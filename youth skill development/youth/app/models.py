from django.db import models

class Sas_view(models.Model):
    java = models.TextField()
    python = models.TextField()
    html = models.TextField()
    ruby = models.TextField()
    datascience = models.TextField()

class Analysis(models.Model):
    skills=models.TextField()
    education_major=models.TextField()
    years_of_experience=models.TextField()