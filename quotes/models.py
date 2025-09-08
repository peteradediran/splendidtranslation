from django.db import models

# Create your models here.
# In quotes/models.py
class QuoteRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    source_language = models.CharField(max_length=50)
    target_language = models.CharField(max_length=50)
    document = models.FileField(upload_to='quote_docs/', blank=True, null=True)
    notes = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Quote from {self.name}"