from django.contrib import admin

from card.models import FlashCard


# Register your models here.
@admin.register(FlashCard)
class ModelFlashCardAdmin(admin.ModelAdmin):
    # list_display = ('question', 'answer')
    pass