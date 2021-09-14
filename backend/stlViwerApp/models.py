from django.db import models
from django.conf import settings
import os


class FileModel(models.Model):
    file = models.FileField(upload_to='documents/', blank=True, null=True)

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.file.name))
        super(FileModel,self).delete(*args,**kwargs)
   
    def __str__(self):
        return str(self.id)

    @property
    def get_keyword_property(self):
        return self.id
