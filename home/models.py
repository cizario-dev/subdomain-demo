from django.db import models
from django.db.models import CharField

# Create your models here.
class Contact(models.Model):
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"