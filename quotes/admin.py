from django.contrib import admin
from .models import QuoteRequest

@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'source_language', 'target_language', 'submitted_at')
    list_filter = ('submitted_at', 'source_language')
    search_fields = ('name', 'email')