# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Movie(models.Model):
    mid = models.AutoField(primary_key=True)
    mname = models.CharField(max_length=255, blank=True, null=True)
    mimg = models.CharField(max_length=255, blank=True, null=True)
    mdesc = models.CharField(max_length=4000, blank=True, null=True)
    mlink = models.CharField(max_length=1100, blank=True, null=True)

    def __str__(self):
        return f'Movie:{self.mid},{self.mname}'


    class Meta:
        managed = False
        db_table = 'movie'
