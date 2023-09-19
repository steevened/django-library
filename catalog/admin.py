from django.contrib import admin
from .models import Author, Book, BookInstance, Genre, Language

# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)


class AuthorAdmin(admin.ModelAdmin):
    pass


class BookAdmin(admin.ModelAdmin):
    pass


class BookInstanceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Author, AuthorAdmin)
