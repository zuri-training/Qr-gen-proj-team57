import imp
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True)
    object_id = models.PositiveBigIntegerField()
    content_object = GenericForeignKey()
    viewed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content_object


    class Meta:
        verbose_name_plural = 'Histories'