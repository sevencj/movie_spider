from django.contrib import admin

# Register your models here.
from movie.models import Movie

admin.site.register(Movie)
