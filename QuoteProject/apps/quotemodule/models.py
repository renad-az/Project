from django.db import models

class Quote(models.Model):
    Tilte = models.CharField(max_length=100)
    text = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
