from django.db import models
from django.core.validators import FileExtensionValidator


class Veedeo(models.Model):
    title = models.CharField(max_length=101, unique=True)
    about = models.TextField(null=True,  blank=True)
    vd_file = models.FileField(upload_to='videos/', validators=[FileExtensionValidator(allowed_extensions=['mp4', 'wmv'])])
    uploaded_tme = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.title