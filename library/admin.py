from django.contrib import admin
from .models import books,categories

# Register your models here.

class book(admin.ModelAdmin):
    prepopulated_fields = {'slug':['name']}
    list_display = ['name','author','date']
admin.site.register(books,book)

class cat(admin.ModelAdmin):
    prepopulated_fields = {'slug':['name']}
admin.site.register(categories,cat)