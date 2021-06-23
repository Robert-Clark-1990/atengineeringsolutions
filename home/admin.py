from django.contrib import admin
from .models import Reviews


class ReviewsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'review',
    )

    ordering = ('name',)


admin.site.register(Reviews, ReviewsAdmin)
