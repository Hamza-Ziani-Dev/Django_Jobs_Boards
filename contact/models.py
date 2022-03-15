from django.db import models


# Create your models here.
class Info(models.Model):
  place = models.CharField(max_length = 150)
  phone_number = models.CharField(max_length = 15)
  email = models.EmailField(max_length=100)
  

  # class Meta:
  #   verbose_name = 'MODELNAME'
  #   verbose_name_plural = 'MODELNAMEs'

  def __str__(self):
    return self.email
