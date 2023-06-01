from django.db import models
import uuid
import user.models
import datetime
# Create your models here.
class Trip(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    creationDate = models.DateTimeField(default=datetime.datetime.now)

    image = models.ImageField(upload_to='postimages', default='post.jpg')
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    startDate = models.DateField()
    endDate = models.DateField(blank=True)
    partySize = models.SmallIntegerField(default=2)
    description = models.TextField()
    
    isReady = models.BooleanField(default=False)

    def __str__(self):
        return self.user
