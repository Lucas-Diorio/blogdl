from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    intro = models.CharField(max_length=255)
    contenido = RichTextUploadingField() # CKEditor Rich Text Field
    imagen = models.ImageField(upload_to='media')
    autor = models.CharField(max_length=255)
    fecha = models.DateField()

    def __str__(self):
        return self.titulo