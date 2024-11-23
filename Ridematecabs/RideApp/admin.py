

# Register your models here.
from django.contrib import admin
from .models import TravelPackage
from django import forms

from .models import Car, CarCategory

@admin.register(TravelPackage)
class TravelPackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration_nights', 'price', 'whatsapp_number', 'image_preview')
    search_fields = ('title', 'destinations')
    readonly_fields = ('image_preview',)


class CarAdminForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'features': forms.Textarea(attrs={'rows': 4}),
            'terms_conditions': forms.Textarea(attrs={'rows': 4}),
        }

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    form = CarAdminForm
    list_display = ('title', 'model', 'category', 'passengers', 'price_per_day', 'price_per_km', 'is_available', 'image_preview')
    list_filter = ('category', 'is_available', 'created_at')
    search_fields = ('title', 'model', 'description')
    readonly_fields = ('image_preview', 'created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('category', 'title', 'model', 'description', 'image', 'image_preview')
        }),
        ('Car Details', {
            'fields': ('passengers', 'features', 'terms_conditions')
        }),
        ('Pricing', {
            'fields': ('price_per_day', 'price_per_km')
        }),
        ('Contact', {
            'fields': ('whatsapp_number',)
        }),
        ('Settings', {
            'fields': ('is_available',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(CarCategory)
class CarCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)