from django.contrib import admin

# Register your models here.
from notation.models import NotationTable, NotesCategories

admin.site.register(NotationTable),
admin.site.register(NotesCategories),