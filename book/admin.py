from django.contrib import admin
from .models import Book, Author
from django.utils.html import format_html

admin.site.register(Author)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "author",
        "name_colored",
        "published_date",
        "thumbnail",
        "is_available",
    )
    # exclude = ("thumbnail",)
    list_filter = ("is_available",)
    # list_per_page = 2
    search_fields = ("name",)
    date_hierarchy = "published_date"
    readonly_fields = ("created_at", "updated_at")

    def name_colored(self, obj):
        if obj.is_available:
            color_code = "00FF00"
        else:
            color_code = "FF0000"
        html = '<span style="color: #{};">{}</span>'.format(color_code, obj.name)
        return format_html(html)

    name_colored.admin_order_field = "name"
    name_colored.short_description = "name color"
