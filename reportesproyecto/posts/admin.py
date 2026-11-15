from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'categoria', 'estado', 'author', 'date')
    list_editable = ('estado',)
    list_filter = ('estado', 'categoria')
    search_fields = ('title', 'body')
    def get_urls(self):
        urls = super().get_urls()

        custom_urls = [
            path(
                "export-reports/",
                self.admin_site.admin_view(
                    self.export_reports_view
                ),
                name="admin-export-reports",
            ),
        ]

        return custom_urls + urls

    def export_reports_view(self, request):
        return redirect("posts:export-reports")