from django.contrib import admin

from job.models import Job, Categorie, Apply

# Register your models here.
admin.site.register(Job)
admin.site.register(Categorie)
admin.site.register(Apply)