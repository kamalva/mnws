from django.contrib import admin
from .models import Entry

class EntryAdmin(admin.ModelAdmin):
    list_display = ("title", "link",)

admin.site.register(Entry, EntryAdmin)
# Register your models here.
