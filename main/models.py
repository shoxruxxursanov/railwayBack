from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
# Create your models here.





def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.doc', '.docx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


def validate_file_size(value):
    filesize= value.size
    
    if filesize < 5120:
        raise ValidationError("The maximum file size that can be uploaded is 5MB")
    else:
        return value
from django.contrib.auth import get_user_model


User = get_user_model()

class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT  )
    fish = models.CharField(max_length=100)
    phone = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    obyektivka = models.FileField(upload_to='files/obyektivka', null=True, blank=True, validators=[validate_file_size,validate_file_extension ])
    turdavoy = models.FileField(upload_to='files/turdavoy', null=True, blank=True, validators=[validate_file_size, validate_file_extension])
    staj = models.IntegerField(default=0)
    lavozim = models.CharField(max_length=200)
    passport = models.CharField(max_length=10)
    id_filial = models.ForeignKey('Filial', on_delete=models.PROTECT, related_name='id_filial')

    def __str__(self) -> str:
        return self.fish


class Filial(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name



