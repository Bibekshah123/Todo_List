from django.db import models
from django.utils import timezone

def user_directory_path(instance, filename):
    # This function generates a path like 'documents/user_<id>/<filename>'
    return f'documents/{filename}'

#model for document
class Document(models.Model):
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
