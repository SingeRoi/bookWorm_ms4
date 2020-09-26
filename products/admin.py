
# Register your models here.
from django.contrib import admin
from .models import Product, Category, Chapter

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'author',
        'isbn',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class ChapterAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'price',
        'translator',
        'author',
        'book',
        'chapter',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Chapter, ChapterAdmin)