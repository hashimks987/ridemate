from django.db import models
from django.utils.html import mark_safe

# Create your models here.
class TravelPackage(models.Model):
    title = models.CharField(max_length=25)
    duration_nights = models.IntegerField()
    duration_days = models.IntegerField()
    destinations = models.TextField(max_length=65)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='packages/')
    whatsapp_number = models.CharField(max_length=20, help_text="Enter WhatsApp number with country code (e.g., 917890123456)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def image_preview(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="100" />')
        return "No Image"
    
    def get_whatsapp_message(self):
        return f"""*{self.title}*%0a
Duration: {self.duration_nights} nights / {self.duration_days} days%0a
Destinations: {self.destinations}%0a
Price: ${self.price}%0a
I'm interested in this package. Please provide more details."""
    
    image_preview.short_description = 'Image Preview'

    


class CarCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Car Categories'

class Car(models.Model):
    category = models.ForeignKey(CarCategory, on_delete=models.CASCADE, related_name='cars')
    title = models.CharField(max_length=21)
    model = models.CharField(max_length=100)
    passengers = models.IntegerField()
    price_per_km = models.DecimalField(max_digits=10, decimal_places=2, help_text="Extra price per kilometer")
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True,max_length=35)
    image = models.ImageField(upload_to='cars/')
    features = models.TextField(help_text="Enter car features, one per line", blank=True)
    terms_conditions = models.TextField(blank=True)
    whatsapp_number = models.CharField(max_length=20, help_text="Enter WhatsApp number with country code (e.g., 917890123456)")
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.model}"
    
    def image_preview(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="100" />')
        return "No Image"
    
    def get_features_list(self):
        return self.features.split('\n') if self.features else []
    
    def get_whatsapp_message(self):
        return f"""*{self.title} - {self.model}*%0a
Passengers: {self.passengers}%0a
Rate: Rs.{self.price_per_day}/day%0a
Extra: Rs.{self.price_per_km}/km%0a
I'm interested in renting this car. Please provide more details."""
    
    image_preview.short_description = 'Image Preview'
    
    class Meta:
        ordering = ['title', 'model']