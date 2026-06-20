from django.db import models

# Theme models

class Sitesettings(models.Model):
    banner = models.ImageField(upload_to = 'banner/')
    caption = models.TextField()
