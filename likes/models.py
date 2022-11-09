from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User

# Create your models here.
class LikedItems:
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete= models.CASCADE)  # type of user liked object 
    object_id = models.PositiveIntegerField()                                 # reading an id 
    content_object = GenericForeignKey()                                      # reading an actual object
