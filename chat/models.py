from django.db import models

class KeyPair(models.Model):
    user_id = models.IntegerField(unique=True)
    public_key = models.TextField()
