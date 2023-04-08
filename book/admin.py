from django.contrib import admin
from .models import Book, Author
from django.db.models import QuerySet

# from django.utils.html import format_html
from django.utils.html import mark_safe


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    list_display_links = ("id", "name")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)
    search_help_text = "search by name here"
    ordering = ("id",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "author",
        # "name_colored",
        "published_date",
        "thumbnail_preview",
        "is_available",
    )
    actions = ("make_books_availaible", )
    list_display_links = ("id", "name")
    list_filter = ("is_available",)
    search_fields = ("name",)
    readonly_fields = ("thumbnail_preview", "created_at", "updated_at")
    autocomplete_fields = ("author",)
    ordering = ("id",)
    save_on_top = True
    save_as = True
    save_as_continue = True
    empty_value_display = "-Пусто-"

    def make_books_availaible(self, request, queryset: QuerySet):
        queryset.update(is_available=True)

    make_books_availaible.short_description = "Make Available"

    def thumbnail_preview(self, obj):
        if obj:
            return mark_safe(
                '<img src="{}" width="150" height="100" />'.format(obj.thumbnail.url)
            )
        return "No photo"

    thumbnail_preview.short_description = "Photo"

    # exclude = ("thumbnail",)
    # list_per_page = 2
    # date_hierarchy = "published_date"
    # raw_id_fields = ("author",)
    # fields = ('name', "is_available", "author",)

    # def name_colored(self, obj):
    #     if obj.is_available:
    #         color_code = "00FF00"
    #     else:
    #         color_code = "FF0000"
    #     html = '<span style="color: #{};">{}</span>'.format(color_code, obj.name)
    #     return format_html(html)

    # name_colored.admin_order_field = "name"
    # name_colored.short_description = "name color"
